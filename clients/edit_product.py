import requests

api_key = "19a77fd089720e974209e222021e788b384f923e"
api_key_2 = "74ca76adec5c53df458f662fc4919f376c49f5f5"

put_url = "http://127.0.0.1:8000/api/product/edit/ywdrsp/"

data = {
    "Title": "Tech writing",
}

authorization = {
    "Authorization": f"Token {api_key}"
}

request = requests.put(url=put_url, headers=authorization, data=data)
print(request.json())