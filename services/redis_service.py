import json
import os

import redis


class RedisService:

    @staticmethod
    def get_user(self):
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        user = redis_client.rpoplpush(os.getenv("REDIS_PRIMARY_USER_TABLE"), os.getenv("REDIS_SECONDARY_USER_TABLE"))
        if user:
            user = json.loads(user)
            self.user_id = user["id"]
            self.name = user["name"]
            self.age = user["age"]
            self.email = user["email"]
            self.phone_number = user["phone_number"]
            self.gender = user["gender"]
            self.password = user["password"]
        else:
            primary_user_table = os.getenv("REDIS_PRIMARY_USER_TABLE")
            secondary_user_table = os.getenv("REDIS_SECONDARY_USER_TABLE")

            os.environ["REDIS_PRIMARY_USER_TABLE"] = secondary_user_table
            os.environ["REDIS_SECONDARY_USER_TABLE"] = primary_user_table

            return RedisService.get_user(self)
        
        self.stagename = os.environ.get("LOCUST_STAGE")