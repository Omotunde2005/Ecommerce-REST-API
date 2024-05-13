import requests

api_key = "19a77fd089720e974209e222021e788b384f923e"
api_key_2 = "74ca76adec5c53df458f662fc4919f376c49f5f5"

post_url = "http://127.0.0.1:8000/api/product/create/"

data = {
    "Title": "Hey there",
    "Description": "Just a normal greeting",
    "Price": 20
}

authorization = {
    "Authorization": f"Token {api_key_2}"
}

files = {
    "Image": open('chat.jpeg', 'rb')
}

request = requests.post(url=post_url, headers=authorization, data=data, files=files)
print(request.json())