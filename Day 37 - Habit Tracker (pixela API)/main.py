import requests

USER = "youruser"
PIXELA_EP = "https://pixe.la/v1/users"
CREATEGRAPH_EP = f"https://pixe.la/v1/users/{USER}/graphs"
GRAPHNAME = "yourgraphname"
GRAPH_EP = f"https://pixe.la/v1/users/{USER}/graphs/{GRAPHNAME}"

header = {
    "X-USER-TOKEN": "yourtoken"
}


## CREATE USER

user_params = {
    "token": "yourtoken",
    "username": "youruser",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_EP, json=user_params)
print(response.json)
print(response.text)

## CREATE GRAPH
graph_params = {
    "id": GRAPHNAME,
    "name": "Any Name",
    "unit": "Any Unit",
    "type": "float",
    "color": "ajisai",
    "timezone": "UTC",
 }

response = requests.post(url=CREATEGRAPH_EP, json=graph_params, headers=header)
print(response.json)
print(response.text)

# POST PIXEL
pixel_param= {
    "date": "20220626",
    "quantity": "1",
}

response = requests.post(url=GRAPH_EP, json=pixel_param, headers=header)
print(response.json)
print(response.text)
