import random

from locust import HttpUser, between, events, task

from cart_entity import CartItemEntity
from configs.test_data import TestData
from services.cart_service import CartService
from services.offer_service import OfferService
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.product_service import ProductService
from services.redis_service import RedisService
from services.user_service import UserService
from utils.common.create_order import calculate_total_price_with_discount
from utils.common.locust_request import LocustRequest
from utils.enums.order_status import OrderStatus
from utils.enums.order_type import OrderType
from utils.enums.payment_card_gateway import PaymentCardGateway
from utils.enums.payment_method import PaymentMethod
from utils.enums.payment_status import PaymentStatus
from utils.enums.product_category import ProductCategory
from utils.enums.user_age import UserType
from utils.payloads.cart import CartPayload
from utils.payloads.order import OrderPayload
from utils.payloads.payment import PaymentPayload


class InStoreOrderSeniorUserWithOfferAndCard(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.order_type = OrderType.IN_STORE.value
        self.payment_method = PaymentMethod.CARD.value
        self.payment_card_gateway = PaymentCardGateway.ADYEN.value
        self.user_type = UserType.SENIOR
        
    @task
    def get_users(self):
        RedisService.get_user(self, self.user_type)
        UserService.get_user(self, self.user_id)

    @task
    def get_offers(self):
        OfferService.get_all_offers(self)
        random_offer = random.choice(self.offers_list)
        self.offer_id = random_offer["id"]
        self.discount_type = random_offer["discount_type"]
        self.discount_value = random_offer["discount_value"]

    @task
    def get_products(self):
        ProductService.get_all_products(self)
        burger_products = [product for product in self.products_list if product["category"] == ProductCategory.BURGER.value]
        random_burger = random.choice(burger_products)
        random_burger_id = random_burger["id"]
        random_burger_price = random_burger["price"]
        dessert_products = [product for product in self.products_list if product["category"] == ProductCategory.DESSERT.value]
        random_dessert = random.choice(dessert_products)
        random_dessert_id = random_dessert["id"]
        random_dessert_price = random_dessert["price"]
        drink_products = [product for product in self.products_list if product["category"] == ProductCategory.DRINK.value]
        random_drink = random.choice(drink_products)
        random_drink_id = random_drink["id"]
        random_drink_price = random_drink["price"]
        side_dish_products = [product for product in self.products_list if product["category"] == ProductCategory.SIDE_DISH.value]
        random_side_dish = random.choice(side_dish_products)
        random_side_dish_id = random_side_dish["id"]
        random_side_dish_price = random_side_dish["price"]
    
        quantity = 5
        self.total_price = (random_burger_price + random_dessert_price + random_drink_price + random_side_dish_price) * quantity

        self.cart_items = [
            CartItemEntity(random_burger_id, quantity=quantity), 
            CartItemEntity(random_dessert_id, quantity=quantity),
            CartItemEntity(random_drink_id, quantity=quantity), 
            CartItemEntity(random_side_dish_id, quantity=quantity)
        ]

    @task
    def create_cart(self):
        payload = CartPayload.create_cart(self.cart_items)
        CartService.create_cart(self, payload)

    @task
    def get_cart(self):
        CartService.get_cart(self, self.cart_id)

    @task
    def create_order(self):
        self.total_price = calculate_total_price_with_discount(self.total_price, self.discount_type, self.discount_value)

        self.expected_order_status = OrderStatus.PENDING.value
        payload = OrderPayload.create_order(self.cart_id, self.order_type, self.offer_id)
        OrderService.create_order(self, payload)

    @task
    def get_order_status(self):
        self.expected_order_status = OrderStatus.PENDING.value
        OrderService.get_order(self, self.order_id)

    @task
    def get_payment_status_by_order_id(self):
        self.expected_payment_status = PaymentStatus.PENDING.value
        PaymentService.get_payment_status_by_order_id(self, self.order_id)

    @task
    def execute_payment(self):
        self.expected_payment_status = PaymentStatus.PAID.value
        payload = PaymentPayload.execute_payment(self.payment_method, self.payment_card_gateway)
        PaymentService.execute_payment(self, payload)

    @task
    def get_payment_status(self):
        self.expected_payment_status = PaymentStatus.PAID.value
        PaymentService.get_payment_status(self, self.payment_id)

    @task
    def get_order_status_2(self):
        self.expected_order_status = OrderStatus.CONFIRMED.value
        OrderService.get_order(self, self.order_id)



class UnitTest(HttpUser):
    tasks = [InStoreOrderSeniorUserWithOfferAndCard]
    host = "https://localhost"
    wait_time = between(1, 2)