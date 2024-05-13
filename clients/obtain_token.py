import requests

post_url = "http://127.0.0.1:8000/api/auth/"

data = {
    "password": "password",
    "username": "email"
}

request = requests.post(url=post_url, data=data)
print(request.json())