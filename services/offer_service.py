import random


class OfferService:

    @staticmethod
    def create_offer(self, payload):
        request_name = f'API_Create_Offer {self.discount_type} {self.stagename}'

        with self.client.post(
            url=f"{self.host}/offer/", 
            name=request_name,
            json=payload,
            headers={"Content-Type": "application/json"},
            catch_response=True   
        ) as response:
            if response.status_code != 201:
                offer_id = payload["id"]
                if response.json()["detail"] == f"Offer with id {offer_id} already exists":
                    payload["id"] = random.randint(1, 1000000)
                    OfferService.create_offer(self, payload)
                else:
                    self.interrupt()
            else:
                self.offer_id = response.json()["id"]

    @staticmethod
    def get_offer(self, offer_id: int):
        request_name = f'API_Get_Offer {self.stagename}'
        with self.client.get(
            url=f"{self.host}/offer/{offer_id}",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()

    @staticmethod
    def get_all_offers(self):
        request_name = f'API_Get_All_Offers {self.stagename}'
        with self.client.get(
            url=f"{self.host}/offer/",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()
            else:
                if len(response.json()['offers']) == 0:
                    self.interrupt()
                self.offers_list = response.json()['offers']