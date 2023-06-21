import requests

url = 'http://127.0.0.1:5000/set'
data = [
    {'key': 'abc', 'value': '1'},
    {'key': 'abc', 'value': '2'},
    {'key': 'xyz', 'value': '1'},
    {'key': 'xyz', 'value': '2'}
]

for item in data:
    response = requests.post(url, json=item)
    print(response.json())
