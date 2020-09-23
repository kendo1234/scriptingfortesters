import requests

url = 'https://api.github.com/users/kendo1234'

response = requests.get(url, headers={'Authorization':'Bearer b18f8789a254494ea549fedbe97ae52fbd1d6247'})

myJson = response.json()
for key in myJson.keys():
    print(key)

print(myJson['id'])