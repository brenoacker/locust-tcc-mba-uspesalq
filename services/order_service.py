from utils.payloads.order import OrderPayload


class OrderService:

    @staticmethod
    def create_order(self, payload: OrderPayload):
        request_name = f'API_Create_Order {self.stagename}'
        with self.client.post(
            url=f"{self.host}/order/", 
            name=request_name,
            json=payload, 
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                self.interrupt()
            else:
                self.order_id = response.json()["id"]

    @staticmethod
    def get_order(self, order_id):
        request_name = f'API_Get_Order {self.stagename}'
        with self.client.get(
            url=f"{self.host}/order/{order_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()
            return response.json()