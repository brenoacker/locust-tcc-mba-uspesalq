import json

import redis


def add_users_to_redis():
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    redis_client.delete("users_primary")
    redis_client.delete("users_secondary")
    redis_client.delete("senior_users_primary")
    redis_client.delete("senior_users_secondary")
    redis_client.delete("mid_users_primary")
    redis_client.delete("mid_users_secondary")
    redis_client.delete("young_users_primary")
    redis_client.delete("young_users_secondary")

    json_file = "utils/data/tb_users.json"
    with open(json_file, 'r') as file:
        data = json.load(file)

    for user in data["tb_users"]:
        if user["age"] >= 65:
            redis_client.rpush("senior_users_primary", json.dumps(user))
        elif user["age"] >= 40:
            redis_client.rpush("mid_users_primary", json.dumps(user))
        elif user["age"] >= 18:
            redis_client.rpush("young_users_primary", json.dumps(user))


def check_redis_keys():
    # Conectar ao Redis
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    keys_to_check = ["young_users_primary", "mid_users_primary", "senior_users_primary"]

    for key in keys_to_check:
        if not redis_client.exists(key):
            add_users_to_redis()
        else:
            print(f"A lista '{key}' já existe no Redis.")

if __name__ == "__main__":
    check_redis_keys()