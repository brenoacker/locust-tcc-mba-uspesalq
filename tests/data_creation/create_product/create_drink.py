import random
import string

from locust import HttpUser, between, task

from configs.test_data import TestData
from services.offer_service import OfferService
from services.product_service import ProductService
from utils.common.create_burger import (generate_unique_burger_name,
                                        generate_unique_drink_name)
from utils.enums.product_category import ProductCategory
from utils.payloads.offer import OfferPayload
from utils.payloads.product import ProductPayload


class CreateDrinkTest(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.product_id = random.randint(1, 1000000)
        self.product_name = generate_unique_drink_name()
        self.product_price = random.randint(1, 100)
        self.product_category = ProductCategory.DRINK

    @task
    def create_product(self):
        payload = ProductPayload.create_product(self.product_id, self.product_name, self.product_price, self.product_category)
        ProductService.create_product(self, payload)

    @task
    def get_product(self):
        ProductService.get_product(self, self.product_id)


class UnitTest(HttpUser):
    tasks = [CreateDrinkTest]
    host = "https://localhost"
    wait_time = between(1, 2)