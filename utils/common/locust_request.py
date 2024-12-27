class LocustRequest:

    @staticmethod
    def fail(self, response):
        response.failure(f"Failed with status code: {response.status_code}, Body: {response.text}")
        self.interrupt()