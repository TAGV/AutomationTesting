import requests


payload ={
             "name": "rock",
             "job": "Actor"
        }

# Getting the response from the API
#response = requests.put("https://reqres.in/api/users/2",data=payload)
response = requests.patch("https://reqres.in/api/users/2",data=payload)

# Printing the response
print(response.json())      # {'name': 'rock', 'job': 'Actor', 'updatedAt': '2022-01-15T16:07:24.432Z'}

assert response.json()['job'] == 'Actor',"Job not match"

