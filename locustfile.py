from locust import HttpUser, task, between
import random
import string

class UserCreationTest(HttpUser):
    wait_time = between(1, 3)  # Tempo de espera entre as requisições
    user_id = None  # ID do usuário criado

    def generate_random_string(self, length=8):
        """Gera uma string aleatória para nomes ou outras informações."""
        return ''.join(random.choices(string.ascii_letters, k=length))

    def generate_random_phone_number(self):
        """Gera um número de telefone aleatório no formato internacional."""
        return f"+1{random.randint(1000000000, 9999999999)}"

    @task
    def create_user(self):
        """Simula a criação de um usuário."""
        # Dados para a requisição
        payload = {
            "name": self.generate_random_string(),
            "email": f"{self.generate_random_string()}@example.com",
            "gender": "male",
            "age": 22,
            "phone_number": self.generate_random_phone_number(),
            "password": "password"
        }

        # Executa a requisição POST
        response = self.client.post(
            "/users/", 
            json=payload, 
            headers={"Content-Type": "application/json"}
        )

        # Loga o resultado
        if response.status_code == 201:  # Sucesso na criação do usuário
            self.environment.events.request.fire(
                request_type="POST",
                name="/users/",
                response_time=response.elapsed.total_seconds() * 1000,  # Convert to milliseconds
                response_length=len(response.content),
                context=self,
                exception=None
            )
            self.user_id = response.json()["id"]
        else:  # Falha na criação do usuário
            self.environment.events.request.fire(
                request_type="POST",
                name="/users/",
                response_time=response.elapsed.total_seconds() * 1000,  # Convert to milliseconds
                response_length=len(response.content),
                context=self,
                exception=Exception(f"Failed with status code: {response.status_code}, Body: {response.text}")
            )

    @task(2)
    def get_user(self):
        if self.user_id is None:
            return
        """Simula a busca de um usuário."""
        # Executa a requisição GET
        response = self.client.get(f"/users/{self.user_id}")

        # Loga o resultado
        if response.status_code == 200:  # Sucesso na busca do usuário
            self.environment.events.request.fire(
                request_type="GET",
                name="/users/user_id",
                response_time=response.elapsed.total_seconds() * 1000,  # Convert to milliseconds
                response_length=len(response.content),
                context=self,
                exception=None
            )
            
        else:  # Falha na busca do usuário
            self.environment.events.request.fire(
                request_type="GET",
                name="/users/user_id",
                response_time=response.elapsed.total_seconds() * 1000,  # Convert to milliseconds
                response_length=len(response.content),
                context=self,
                exception=Exception(f"Failed with status code: {response.status_code}, Body: {response.text}")
            )