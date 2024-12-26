from configs.test_data import TestData
import random
from configs.test_data import TestData
from locust import task, HttpUser
from services.product_service import ProductService
from utils.common.create_burger import generate_unique_side_dish_name
from utils.enums.product_category import ProductCategory
from utils.payloads.product import ProductPayload

class CreateSideDishTest(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.product_id = random.randint(1, 1000000)
        self.product_name = generate_unique_side_dish_name()
        self.product_price = random.randint(1, 100)
        self.product_category = ProductCategory.SIDE_DISH

    @task
    def create_product(self):
        payload = ProductPayload.create_product(self.product_id, self.product_name, self.product_price, self.product_category)
        ProductService.create_product(self, payload)

    @task
    def get_product(self):
        ProductService.get_product(self, self.product_id)


class UnitTest(HttpUser):
    tasks = [CreateSideDishTest]
    host = "https://localhost"