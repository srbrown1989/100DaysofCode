import os
import requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

QUANTITY = "6"

pixel_config = {
    "date": dt.datetime.today().strftime("%Y%m%d"),
    "quantity": input("How many hours have you coded today?")
}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)