import json

import requests


payload = open("payload.json",'r').read()

post_data = requests.post("https://reqres.in/api/users",data=json.loads(payload))

print(post_data.json())

assert post_data.json()['name'] == 'Roger',"Name not match"

# Response Header keywords
print(post_data.headers.get("Content-type"))
print(post_data.headers.get("date"))
print(post_data.headers.get("server"))

