import requests



#response = requests.get('https://the-internet.herokuapp.com/basic_auth',auth=('sfs','sfsf'))   #Authentication Error = 401
response = requests.get('https://the-internet.herokuapp.com/basic_auth',auth=('admin','admin'))

print(response.status_code)