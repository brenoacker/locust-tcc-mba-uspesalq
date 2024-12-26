class PaymentService:
    @staticmethod
    def execute_payment(self, payload):
        request_name = f'API_Execute_Payment {self.stagename}'

        with self.client.post(
            url=f"{self.host}/payment/{self.order_id}", 
            name=request_name,
            json=payload,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                self.interrupt()
            self.payment_id = response.json()["id"]

    @staticmethod
    def get_payment_status(self, payment_id):
        request_name = f'API_Get_Payment_Status {self.stagename}'

        with self.client.get(
            url=f"{self.host}/payment/id/{payment_id}",
            name=request_name,
            headers={"Content-Type": "application/json", "user-id": self.user_id},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()
            return response.json()