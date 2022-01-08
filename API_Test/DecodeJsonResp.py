import requests

param = {'page':2}
resp = requests.get("https://reqres.in/api/users",params=param)  #Parameter passing and then check the url
print(resp.url)

json_response = resp.json()
print((json_response))

# Validating the JSON Response
print(len(json_response['data']))
assert len(json_response['data']) == 6,"The length does not match"

print((json_response['total']))
assert json_response['total'] == 12,"Number is incorrect"

print(json_response['data'][0]['last_name'])
#print(json_response['data'][1])
assert json_response['data'][0]['last_name'] == "Lawson","Name not matching"

assert json_response['data'][0]['first_name'] != None,"Name not matching"

email = (json_response['data'][0]['email'])
print(type(email))
assert str(email).endswith('reqres.in'),"Email mismatch"