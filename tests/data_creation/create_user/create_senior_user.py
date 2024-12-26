import random
import string
from configs.test_data import TestData
from locust import task, HttpUser
from services.user_service import UserService
from utils.common.create_user import generate_random_age, generate_random_email, generate_random_gender, generate_random_phone_number, generate_random_string
from utils.payloads.user import UserPayload

class CreateSeniorUserTest(TestData):

    def __init__(self, parent):
        super().__init__(parent)
        self.user_id = None
        self.name = generate_random_string()
        self.email = generate_random_email()
        self.age = generate_random_age([65,100])
        self.phone_number = generate_random_phone_number()
        self.gender = generate_random_gender()
        self.password = generate_random_string()


    

    @task
    def create_user(self):
        payload = UserPayload.create_user(self.name, self.email, self.age, self.gender, self.phone_number, self.password)
        UserService.create_senior_user(self, payload)

    @task
    def get_user(self):
        UserService.get_user(self, self.user_id)


    
class UnitTest(HttpUser):
    tasks = [CreateSeniorUserTest]
    host = "https://localhost"