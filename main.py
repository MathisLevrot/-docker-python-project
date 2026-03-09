import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

print("Status code :", response.status_code)
print("Content :", response.json())
