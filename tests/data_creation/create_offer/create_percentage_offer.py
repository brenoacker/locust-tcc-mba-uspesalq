from configs.test_data import TestData
import random
import string
from configs.test_data import TestData
from locust import task, HttpUser
from services.offer_service import OfferService
from utils.enums.offer_type import OfferType
from utils.payloads.offer import OfferPayload

class CreatePercentageOfferTest(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.offer_id = random.randint(1000, 1000000)
        self.discount_type = OfferType.PERCENTAGE
        self.discount_value = random.randint(1, 100)
        self.expiration_days = 30

    @task
    def create_offer(self):
        payload = OfferPayload.create_offer(self.offer_id, self.discount_type, self.discount_value, self.expiration_days)
        OfferService.create_offer(self, payload)

    @task
    def get_offer(self):
        OfferService.get_offer(self, self.offer_id)

class UnitTest(HttpUser):
    tasks = [CreatePercentageOfferTest]
    host = "https://localhost"