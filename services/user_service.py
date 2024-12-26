from utils.payloads.user import UserPayload

class UserService:

    @staticmethod
    def create_mid_age_user(self, payload: UserPayload):
        UserService.create_user(self, payload, "mid_age")

    @staticmethod
    def create_senior_user(self, payload: UserPayload):
        UserService.create_user(self, payload, "senior")

    @staticmethod
    def create_young_user(self, payload: UserPayload):
        UserService.create_user(self, payload, "young")

    @staticmethod
    def create_user(self, payload: UserPayload, user_age):
        request_name = f'API_Create_User {user_age} {self.stagename}'
        
        with self.client.post(
            url=f"{self.host}/users/", 
            name=request_name,
            json=payload, 
            headers={"Content-Type": "application/json"},
            catch_response=True
        ) as response:
            if response.status_code != 201:
                self.interrupt()
            else:
                self.user_id = response.json()["id"]

    @staticmethod
    def get_user(self, user_id):
        request_name = f'API_Get_User {self.stagename}'
        with self.client.get(
            url=f"{self.host}/users/{user_id}",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()

    @staticmethod
    def get_all_users(self):
        request_name = f'API_Get_All_Users {self.stagename}'
        with self.client.get(
            url=f"{self.host}/users/",
            name=request_name,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                self.interrupt()
            else:
                if len(response.json()['users']) == 0:
                    self.interrupt()
                self.users_list = response.json()['users']