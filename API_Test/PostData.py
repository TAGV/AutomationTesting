import requests


payload ={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

# Getting the response from the API
response = requests.post("https://reqres.in/api/register",data=payload)

# Printing the response
print(response.json())      # {'id': 4, 'token': 'QpwL5tke4Pnpja7X4'}

assert response.json()['id'] == 4,"ID not match"

