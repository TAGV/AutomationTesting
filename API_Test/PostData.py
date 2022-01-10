import requests


payload ={
            "name": "Jack",
            "job": "Doctor"
        }

post_data = requests.post("https://reqres.in/api/users",data=payload)

print(post_data.json())

assert post_data.json()['name'] == 'Jack',"Name not match"

