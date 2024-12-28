import json

import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

redis_client.delete("users_primary")
redis_client.delete("users_secondary")

json_file = "utils/data/tb_users.json"
with open(json_file, 'r') as file:
    data = json.load(file)

for user in data["tb_users"]:
    redis_client.rpush("users_primary", json.dumps(user))