import requests

url = "https://jsonplaceholder.typicode.com/photos"
# response = requests.get(url)
#
# print(response.json())


jsonPayload = {'name':'ken', 'age':36,'url':'test.com', 'thumbnailUrl':'test.com'}

response = requests.post(url, json=jsonPayload)

print(response.json())


