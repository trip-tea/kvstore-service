import requests

base_url = 'http://127.0.0.1:5000/get/'
keys = ['abc', 'xyz']

for key in keys:
    url = base_url + key
    response = requests.get(url)
    print(response.json())
