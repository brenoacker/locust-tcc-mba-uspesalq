# import json
# import os

# import redis


# class RedisService:

#     @staticmethod
#     def get_user(self):
#         redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
#         user = redis_client.rpoplpush(os.getenv("REDIS_PRIMARY_USER_TABLE"), os.getenv("REDIS_SECONDARY_USER_TABLE"))
#         if user:
#             user = json.loads(user)
#             self.user_id = user["id"]
#             self.name = user["name"]
#             self.age = user["age"]
#             self.email = user["email"]
#             self.phone_number = user["phone_number"]
#             self.gender = user["gender"]
#             self.password = user["password"]
#         else:
#             primary_user_table = os.getenv("REDIS_PRIMARY_USER_TABLE")
#             secondary_user_table = os.getenv("REDIS_SECONDARY_USER_TABLE")

#             os.environ["REDIS_PRIMARY_USER_TABLE"] = secondary_user_table
#             os.environ["REDIS_SECONDARY_USER_TABLE"] = primary_user_table

#             return RedisService.get_user(self)
        
#         self.stagename = os.environ.get("LOCUST_STAGE")

import json
import os

import redis


class RedisService:

    def __init__(self):
        self.user_id = None
        self.name = None
        self.age = None
        self.email = None
        self.phone_number = None
        self.gender = None
        self.password = None
        self.stagename = os.environ.get("LOCUST_STAGE")

    @staticmethod
    def move_user_script():
        """
        Script Lua para mover um item da tabela primária para a secundária.
        """
        return """
        local item = redis.call('RPOP', KEYS[1])
        if item then
            redis.call('LPUSH', KEYS[2], item)
        end
        return item
        """

    def get_user(self):
        """
        Obtém um usuário de uma tabela Redis, movendo-o de uma tabela primária para uma secundária.
        """
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        primary_user_table = os.getenv("REDIS_PRIMARY_USER_TABLE")
        secondary_user_table = os.getenv("REDIS_SECONDARY_USER_TABLE")

        # Executa o script Lua para mover o usuário
        user = redis_client.eval(
            RedisService.move_user_script(),
            2,
            primary_user_table,
            secondary_user_table
        )

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
            # Troca as tabelas se a primária estiver vazia
            os.environ["REDIS_PRIMARY_USER_TABLE"] = secondary_user_table
            os.environ["REDIS_SECONDARY_USER_TABLE"] = primary_user_table
            return RedisService.get_user(self)  # Recursivamente tenta obter o usuário

        return self
