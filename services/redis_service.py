import json
import os

import redis

from utils.enums.user_age import UserType


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

    def get_user(self, user_type: UserType):
        """
        Obtém um usuário de uma tabela Redis, movendo-o de uma tabela primária para uma secundária.
        """

        primary_user_table_value, secondary_user_table_value = RedisService.get_table_value_by_user_type(user_type)
        primary_env_table, secondary_env_table = RedisService.get_env_table_by_user_type(user_type)
        redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Executa o script Lua para mover o usuário
        user = redis_client.eval(
            RedisService.move_user_script(),
            2,
            primary_user_table_value,
            secondary_user_table_value
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
            os.environ[primary_env_table] = secondary_user_table_value
            os.environ[secondary_env_table] = primary_user_table_value
            return RedisService.get_user(self)  # Recursivamente tenta obter o usuário

        return self

    def get_table_value_by_user_type(user_type: UserType):

        if user_type == UserType.SENIOR:
            return os.getenv("REDIS_PRIMARY_SENIOR_USER_TABLE"), os.getenv("REDIS_SECONDARY_SENIOR_USER_TABLE")
        elif user_type == UserType.MID_AGE:
            return os.getenv("REDIS_PRIMARY_MID_AGE_USER_TABLE"), os.getenv("REDIS_SECONDARY_MID_AGE_USER_TABLE")
        elif user_type == UserType.YOUNG:
            return os.getenv("REDIS_PRIMARY_YOUNG_USER_TABLE"), os.getenv("REDIS_SECONDARY_YOUNG_USER_TABLE")
        else:
            raise Exception("Invalid user type")
        
    def get_env_table_by_user_type(user_type: UserType):
        if user_type == UserType.SENIOR:
            return "REDIS_PRIMARY_SENIOR_USER_TABLE", "REDIS_SECONDARY_SENIOR_USER_TABLE"
        elif user_type == UserType.MID_AGE:
            return "REDIS_PRIMARY_MID_AGE_USER_TABLE", "REDIS_SECONDARY_MID_AGE_USER_TABLE"
        elif user_type == UserType.YOUNG:
            return "REDIS_PRIMARY_YOUNG_USER_TABLE", "REDIS_SECONDARY_YOUNG_USER_TABLE"
        else:
            raise Exception("Invalid user type")