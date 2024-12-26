from configs.features_weight import FeaturesWeight
from configs.test_data import TestData
from configs.test_stages import TestStagesConfig
from locust import run_single_user, HttpUser, LoadTestShape

class HttpCollection(HttpUser):
    host = "https://localhost"
    tasks = FeaturesWeight.get_features_weight()

class CollectionShape(LoadTestShape):
    stagename: str = ""
    stages = TestStagesConfig.get_stages()
    current_stage = 0
    start_time = None

    def on_start(self):
        # Configurar o cliente HTTP para usar o proxy do Fiddler
        self.client.proxies = {
            "http": "http://localhost:8888",
            "https": "http://localhost:8888"
        }

    def tick(self):
        run_time = self.get_run_time()

        # if self.current_stage < len(self.stages):
        #     stage = self.stages[self.current_stage]
        #     self.stagename = stage["name"]
        #     TestData.stagename = self.stagename
        #     if run_time > stage["duration"]:
        #         self.current_stage += 1
        #         if self.current_stage >= len(self.stages):
        #             return None
        #         stage = self.stages[self.current_stage]
        #         self.start_time = run_time
        #     return (stage["users"], stage["spawn_rate"])
        
        # return None

        for stage in self.stages:
            if run_time < stage["duration"]:
                if self.stagename != stage["name"]:
                    self.stagename = stage["name"]
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None

if __name__ == "__main__":
    run_single_user(HttpCollection)