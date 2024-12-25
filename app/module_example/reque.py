import requests

response = requests.get('http://date.jsontest.com/')
data = response.json()
print(data)
a=data.get('milliseconds_since_epoch')
print(type(a))

