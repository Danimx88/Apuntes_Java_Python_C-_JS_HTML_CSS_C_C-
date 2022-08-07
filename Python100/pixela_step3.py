import requests

USERNAME = "USER"
TOKEN = "PASSWORD"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

#user_params = {
#    "token": TOKEN,
#    "username": USERNAME,
#    "agreeTermsOfService": "yes",
#    "notMinor": "yes",
#}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
        "id": GRAPH_ID,
        "name": "Cycle Graph",
        "unit": "Hr",
        "type": "float",
        "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


pixel_data = {
        "date": "20220806",
        "quantity": "12",
}


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
