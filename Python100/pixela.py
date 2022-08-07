import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hklmds95e9534kmv546dgh4",
    "username": "danielmx88",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
