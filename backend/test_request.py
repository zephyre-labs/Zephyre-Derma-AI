import requests

url = "http://localhost:5000/analyze"
payload = {}

response = requests.post(url, json=payload)
print(response.json())
