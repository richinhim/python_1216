import requests

url = "https://httpbin.org/post"

data = {'key1': 'value1', 'key2':'value2'}

response = requests.post(url, data)

print(response.text)