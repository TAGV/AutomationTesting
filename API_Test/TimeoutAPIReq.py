import requests


#response = requests.get("https://httpbin.org/delay/10",timeout=5) #ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=5)
response = requests.get("https://httpbin.org/delay/3",timeout=5)   #Delay = 3 sec, so it will work

print(response.status_code)

print(response.json())
print(response.json()['headers'])
print(response.json()['headers']['X-Amzn-Trace-Id'])

#assert response.json()['headers']['X-Amzn-Trace-Id'] == 'Root=1-61e2ffcc-27e5bf1d7b6db3ce1bcb9de9',"No root"

print(response.headers)

assert response.headers['content-type'] == 'application/json','Wrong'