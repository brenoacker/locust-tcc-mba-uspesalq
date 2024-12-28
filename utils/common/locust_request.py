class LocustRequest:

    @staticmethod
    def fail(self, response, message = None):
        if message:
            response.failure(message)
            self.interrupt()
        response.failure(f"Failed with status code: {response.status_code}, Body: {response.text}")
        self.interrupt()