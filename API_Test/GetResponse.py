import requests


resp = requests.get("https://reqres.in/api/users?page=2")
code = resp.status_code
assert code==200,f"The code {code} is not matching"

#print(type(resp))   #<class 'requests.models.Response'>
#print(dir(resp))

#print(resp.text)
#print(resp.content)
print(resp.json())   # Copy the text and check the response on http://jsonviewer.stack.hu/
print()
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)
print(resp.links)
