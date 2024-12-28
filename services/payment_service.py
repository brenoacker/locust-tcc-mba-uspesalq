from utils.common.locust_request import LocustRequest


class PaymentService:
    @staticmethod
    def execute_payment(self, payload):
        request_name = f'API_Execute_Payment{self.stagename}'
        request_name += '_with_offer' if self.offer_id else '_without_offer'

        with self.client.post(
            url=f"{self.host}/payment/{self.order_id}", 
            name=request_name,
            json=payload,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                LocustRequest.fail(self, response)

            json_response = response.json()

            if json_response["payment_method"] != self.payment_method:
                LocustRequest.fail(self, response, f"Payment method is {json_response['payment_method']}, expected {self.payment_method}")

            if json_response["payment_card_gateway"] != self.payment_card_gateway:
                LocustRequest.fail(self, response, f"Payment card gateway is {json_response['payment_card_gateway']}, expected {self.payment_card_gateway}")

            if json_response["order_id"] != self.order_id:
                LocustRequest.fail(self, response, f"Order ID is {json_response['order_id']}, expected {self.order_id}")

            if json_response["user_id"] != self.user_id:
                LocustRequest.fail(self, response, f"User ID is {json_response['user_id']}, expected {self.user_id}")

            if json_response["status"] != self.expected_payment_status:
                LocustRequest.fail(self, response, f"Payment status is {json_response['status']}, expected {self.expected_payment_status}")

            self.payment_id = json_response["id"]

    @staticmethod
    def get_payment_status(self, payment_id):
        request_name = f'API_Get_Payment_Status{self.stagename}'

        with self.client.get(
            url=f"{self.host}/payment/id/{payment_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)
            
            json_response = response.json()

            if json_response["status"] != self.expected_payment_status:
                LocustRequest.fail(self, response, f"Payment status is {json_response['status']}, expected {self.expected_payment_status}")

            if json_response["payment_method"] != self.payment_method:
                LocustRequest.fail(self, response, f"Payment method is {json_response['payment_method']}, expected {self.payment_method}")

            if json_response["payment_card_gateway"] != self.payment_card_gateway:
                LocustRequest.fail(self, response, f"Payment card gateway is {json_response['payment_card_gateway']}, expected {self.payment_card_gateway}")

            if json_response["order_id"] != self.order_id:
                LocustRequest.fail(self, response, f"Order ID is {json_response['order_id']}, expected {self.order_id}")

            if json_response["user_id"] != self.user_id:
                LocustRequest.fail(self, response, f"User ID is {json_response['user_id']}, expected {self.user_id}")

    @staticmethod
    def get_payment_status_by_order_id(self, order_id):
        request_name = f'API_Get_Payment_Status_By_Order_Id{self.stagename}'

        with self.client.get(
            url=f"{self.host}/payment/order/{order_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                LocustRequest.fail(self, response)
            
            json_response = response.json()

            if json_response["status"] != self.expected_payment_status:
                LocustRequest.fail(self, response, f"Payment status is {json_response['status']}, expected {self.expected_payment_status}")

            if json_response["order_id"] != self.order_id:
                LocustRequest.fail(self, response, f"Order ID is {json_response['order_id']}, expected {self.order_id}")

            if json_response["user_id"] != self.user_id:
                LocustRequest.fail(self, response, f"User ID is {json_response['user_id']}, expected {self.user_id}")