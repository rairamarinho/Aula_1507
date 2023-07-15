import json

json_data = '{"id": 1, "nome": "Raíra", "saldo": 100000.00 }'
data = json.loads(json_data)

print(data["id"])
print(data["nome"])
print(data["saldo"])