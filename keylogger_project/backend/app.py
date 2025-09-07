import requests

url = "http://127.0.0.1:5000/api/upload"
payload = {
    "machine": "PC-5",
    "data": "שלום"
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
