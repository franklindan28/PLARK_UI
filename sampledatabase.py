import requests

URL = "https://trashcash.ph/api/v1/auth/sign_in"

response = requests.get(URL)

print(response.text)