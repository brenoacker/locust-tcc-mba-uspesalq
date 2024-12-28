from utils.common.locust_request import LocustRequest
from utils.payloads.order import OrderPayload


class OrderService:

    @staticmethod
    def create_order(self, payload: OrderPayload):
        request_name = f'API_Create_Order{self.stagename}'
        request_name += ' with offer' if self.offer_id else ' without offer'
        with self.client.post(
            url=f"{self.host}/order/", 
            name=request_name,
            json=payload, 
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                LocustRequest.fail(self, response)
            else:
                json_response = response.json()

                if json_response["cart_id"] != self.cart_id:
                    LocustRequest.fail(self, response, f"Cart ID is {json_response['cart_id']}, expected {self.cart_id}")

                if json_response["user_id"] != self.user_id:
                    LocustRequest.fail(self, response, f"User ID is {json_response['user_id']}, expected {self.user_id}")

                if json_response["type"] != self.order_type:
                    LocustRequest.fail(self, response, f"Order type is {json_response['type']}, expected {self.order_type}")

                if json_response["status"] != self.expected_order_status:
                    LocustRequest.fail(self, response, f"Order status is {json_response['status']}, expected {self.expected_order_status}")

                if json_response["total_price"] != self.total_price:
                    LocustRequest.fail(self, response, f"Total price is {json_response['total_price']}, expected {self.total_price}")

                if json_response["offer_id"] != self.offer_id:
                    LocustRequest.fail(self, response, f"Offer ID is {json_response['offer_id']}, expected {self.offer_id}")

                self.order_id = json_response["id"]

    @staticmethod
    def get_order(self, order_id):
        request_name = f'API_Get_Order{self.stagename}'
        with self.client.get(
            url=f"{self.host}/order/{order_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)
            json_response = response.json()

            if json_response["cart_id"] != self.cart_id:
                LocustRequest.fail(self, response, f"Cart ID is {json_response['cart_id']}, expected {self.cart_id}")

            if json_response["user_id"] != self.user_id:
                LocustRequest.fail(self, response, f"User ID is {json_response['user_id']}, expected {self.user_id}")

            if json_response["type"] != self.order_type:
                LocustRequest.fail(self, response, f"Order type is {json_response['type']}, expected {self.order_type}")

            if json_response["status"] != self.expected_order_status:
                LocustRequest.fail(self, response, f"Order status is {json_response['status']}, expected {self.expected_order_status}")

            if json_response["total_price"] != self.total_price:
                LocustRequest.fail(self, response, f"Total price is {json_response['total_price']}, expected {self.total_price}")

            if json_response["offer_id"] != self.offer_id:
                LocustRequest.fail(self, response, f"Offer ID is {json_response['offer_id']}, expected {self.offer_id}")

            return response.json()