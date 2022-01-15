import json

import requests

#Opening the JSON file
payload = open("payload.json",'r').read()

# Sending the payload to API
post_data = requests.post("https://reqres.in/api/users",data=json.loads(payload))

# Getting the response from the API
response = post_data.json()          #{'name': 'Roger', 'job': 'Doctor', 'id': '521', 'createdAt': '2022-01-15T14:50:59.673Z'}

# Printing the API response
print(response)


assert post_data.json()['name'] == 'Roger',"Name not match"

# Response Header keywords
print(post_data.headers.get("Content-type"))
print(post_data.headers.get("date"))
print(post_data.headers.get("server"))

