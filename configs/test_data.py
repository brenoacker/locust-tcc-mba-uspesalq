import os

from locust import SequentialTaskSet, events

from utils.enums.offer_type import OfferType
from utils.enums.order_type import OrderType
from utils.enums.payment_card_gateway import PaymentCardGateway
from utils.enums.payment_method import PaymentMethod
from utils.enums.product_category import ProductCategory
from utils.enums.user_age import UserType


class TestData(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_id = None
        self.users_list = []
        self.name = None
        self.email = None
        self.age = None
        self.phone_number = None
        self.gender = None
        self.password = None
        self.host = "http://localhost:8000"
        self.offer_id = None
        self.discount_type: OfferType = None
        self.discount_value = None
        self.expiration_days = None
        self.product_id = None
        self.product_name = None
        self.product_price = None
        self.product_category: ProductCategory = None
        self.offers_list = []
        self.products_list = []
        self.cart_items = []
        self.cart_id = None
        self.order_type: OrderType = None
        self.order_id = None
        self.payment_id = None
        self.payment_method: PaymentMethod = None
        self.payment_card_gateway: PaymentCardGateway = None
        self.expected_payment_status = None
        self.expected_order_status = None
        self.total_price: float = None
        self.user_type: UserType = None

        self.client.trust_env = True
        self.client.verify = False
        self.client.proxies = {"http": "http://localhost:8888", "https": "https://localhost:8888"}
        
        self.redis_primary_user_table = "users_primary"
        self.redis_secondary_user_table = "users_secondary"

        self.stagename = None

    def test_reset(self):
        self.stagename = os.environ.get("LOCUST_STAGE")