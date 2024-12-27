import random
import string

from utils.common.create_burger import generate_unique_burger_name
from utils.common.locust_request import LocustRequest


class ProductService:

    @staticmethod
    def create_product(self, payload):
        request_name = f'API_Create_Product_{self.product_category}{self.stagename}'

        with self.client.post(
            url=f'{self.host}/products/', 
            name=request_name,
            json=payload,
            headers={"Content-Type": "application/json"},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                product_id = payload["id"]
                product_name = payload["name"]
                if response.json()["detail"] == f"Product with '{product_name}' name already registered":
                    payload["name"] = generate_unique_burger_name()
                    ProductService.create_product(self, payload)
                elif response.json()["detail"] == f"Product id '{product_id}' already registered":
                    payload["id"] = random.randint(1, 1000000)
                    ProductService.create_product(self, payload)
                else:
                    LocustRequest.fail(self, response)
            else:
                self.product_id = response.json()["id"]

    @staticmethod
    def get_product(self, product_id):
        request_name = f'API_Get_Product{self.stagename}'
        with self.client.get(
            url=f"{self.host}/products/{product_id}",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)

    @staticmethod
    def get_all_products(self):
        request_name = f'API_Get_All_Products{self.stagename}'
        with self.client.get(
            url=f"{self.host}/products/",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)
            else:
                self.products_list = response.json()["products"]