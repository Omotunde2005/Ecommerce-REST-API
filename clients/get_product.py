import requests

api_key = "19a77fd089720e974209e222021e788b384f923e"

get_url = "http://127.0.0.1:8000/api/products/"

authorization = {
    "Authorization": f"Token {api_key}"
}

request = requests.get(url=get_url, headers=authorization)
print(request.json())