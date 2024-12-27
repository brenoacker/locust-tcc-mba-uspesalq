from abc import abstractmethod

from utils.common.locust_request import LocustRequest


class CartService:

    @abstractmethod
    def create_cart(self, payload):
        request_name = f'API_Create_Cart{self.stagename}'

        with self.client.post(
            url=f'{self.host}/cart/', 
            name=request_name,
            json=payload,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                LocustRequest.fail(self, response)
            else:
                self.cart_id = response.json()['id']
    
    @abstractmethod
    def get_cart(self, cart_id):
        request_name = f'API_Get_Cart{self.stagename}'
        with self.client.get(
            url=f"{self.host}/cart/{cart_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)