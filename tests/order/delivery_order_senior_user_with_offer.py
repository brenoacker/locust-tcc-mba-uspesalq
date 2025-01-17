from cart_entity import CartItemEntity
from configs.test_data import TestData
import random
from configs.test_data import TestData
from locust import task, HttpUser
from services.cart_service import CartService
from services.offer_service import OfferService
from services.order_service import OrderService
from services.payment_service import PaymentService
from services.product_service import ProductService
from services.user_service import UserService
from utils.common.create_burger import generate_unique_side_dish_name
from utils.common.create_user import generate_random_age, generate_random_email, generate_random_gender, generate_random_phone_number, generate_random_string
from utils.enums.order_status import OrderStatus
from utils.enums.order_type import OrderType
from utils.enums.payment_card_gateway import PaymentCardGateway
from utils.enums.payment_method import PaymentMethod
from utils.enums.payment_status import PaymentStatus
from utils.enums.product_category import ProductCategory
from utils.payloads.cart import CartPayload
from utils.payloads.order import OrderPayload
from utils.payloads.payment import PaymentPayload
from utils.payloads.product import ProductPayload
from utils.payloads.user import UserPayload

class DeliveryOrderSeniorUserWithOffer(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.user_id = None
        self.name = generate_random_string()
        self.email = generate_random_email()
        self.age = generate_random_age([65,100])
        self.phone_number = generate_random_phone_number()
        self.gender = generate_random_gender()
        self.password = generate_random_string()
        self.order_type = OrderType.DELIVERY.value
        self.payment_method = PaymentMethod.CARD.value
        self.payment_card_gateway = PaymentCardGateway.ADYEN.value
        
    @task
    def get_users(self):
        UserService.get_all_users(self)
        self.user_id = random.choice(self.users_list)["id"]

    @task
    def get_offers(self):
        OfferService.get_all_offers(self)
        self.offer_id = random.choice(self.offers_list)["id"]

    @task
    def get_products(self):
        ProductService.get_all_products(self)
        burger_products = [product for product in self.products_list if product["category"] == ProductCategory.BURGER.value]
        random_burger = random.choice(burger_products)["id"]
        dessert_products = [product for product in self.products_list if product["category"] == ProductCategory.DESSERT.value]
        random_dessert = random.choice(dessert_products)["id"]
        drink_products = [product for product in self.products_list if product["category"] == ProductCategory.DRINK.value]
        random_drink = random.choice(drink_products)["id"]
        side_dish_products = [product for product in self.products_list if product["category"] == ProductCategory.SIDE_DISH.value]
        random_side_dish = random.choice(side_dish_products)["id"]
    

        self.cart_items = [
            CartItemEntity(random_burger, quantity=5), 
            CartItemEntity(random_dessert, quantity=5),
            CartItemEntity(random_drink, quantity=5), 
            CartItemEntity(random_side_dish, quantity=5)
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
        payload = OrderPayload.create_order(self.cart_id, self.order_type, self.offer_id)
        OrderService.create_order(self, payload)

    @task
    def get_order_status(self):
        order = OrderService.get_order(self, self.order_id)
        if order["status"] != OrderStatus.PENDING.value:
            self.interrupt()

    @task
    def execute_payment(self):
        payload = PaymentPayload.execute_payment(self.payment_method, self.payment_card_gateway)
        PaymentService.execute_payment(self, payload)

    @task
    def get_payment_status(self):
        payment = PaymentService.get_payment_status(self, self.payment_id)
        if payment["status"] != PaymentStatus.PAID.value:
            self.interrupt()

    @task
    def get_order_status_2(self):
        order = OrderService.get_order(self, self.order_id)
        if order["status"] != OrderStatus.CONFIRMED.value:
            self.interrupt()

        if order["type"] != self.order_type:
            self.interrupt()



class UnitTest(HttpUser):
    tasks = [DeliveryOrderSeniorUserWithOffer]
    host = "https://localhost"