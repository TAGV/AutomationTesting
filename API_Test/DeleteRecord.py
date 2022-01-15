import requests


# Getting the response from the API
response = requests.delete("https://reqres.in/api/users/2")

# Printing the response code
print(response.status_code)      #204

assert response.status_code == 204,"Failed to delete the record"

