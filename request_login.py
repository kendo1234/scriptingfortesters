import requests

url = 'https://api.github.com/users/kendo1234'


# Insecure
# response = requests.get(url, auth=('user', 'password'))

# More secure
response = requests.get(url, headers={'Authorization':'Bearer b18f8789a254494ea549fedbe97ae52fbd1d6247'})


print(response.json())