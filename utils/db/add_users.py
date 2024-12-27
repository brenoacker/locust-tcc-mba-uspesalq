# Realizar a separacao dos usuarios nos tres grupos de acordo com a idade em tabelas diferentes

# Criar script para adicao de ofertas no pg

# Criar script para adicao de produtos no pg


import json

import redis
import requests

json_file = "utils/data/tb_users.json"
with open(json_file, 'r') as file:
    data = json.load(file)

users = []

for user in data["tb_users"]:
    response = requests.post(
        url="http://localhost:8000/users/", 
        json=user, 
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 201:
        print(f"Usuário {user['id']} adicionado com sucesso!")
        users.append(response.json())
    else:
        print(f"Falha ao adicionar usuário {user['id']}: {response.status_code} - {response.text}")

users_json = {"users": users}
with open("utils/data/users.json", 'w') as file:
    json.dump(users_json, file)

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

redis_client.delete("users_primary")
redis_client.delete("users_secondary")

json_file = "utils/data/users.json"
with open(json_file, 'r') as file:
    data = json.load(file)

for user in data["users"]:
    redis_client.rpush("users_primary", json.dumps(user))

print("Usuários adicionados ao Redis com sucesso!")