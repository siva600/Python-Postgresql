# https://jsonplaceholder.typicode.com/users


import requests
import json

# data = requests.get("https://jsonplaceholder.typicode.com/users")

response = requests.get("https://jsonplaceholder.typicode.com/users")
# while data_status.raise_for_status() is True:
json_data = json.loads(response.text)
for item in json_data:
        print(item['name'], ":", item['address']['city'])
