import requests
from datetime import datetime


MY_PAGE = "https://pixe.la/@mirek33"
MY_GRAPH = "https://pixe.la/v1/users/mirek33/graphs/graph1.html"


TOKEN = "asdfghjklzxcvbnm"
USERNAME = "mirek33"
GRAPH_ID = "graph1"
QUANTITY = input("How many minutes did spend for coding? ")


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
today = datetime.now().date().strftime("%Y%m%d")
headers = {"X-USER-TOKEN": TOKEN}


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


graph_params = {
    "id": GRAPH_ID,
    "name": "coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_params = {
  "quantity": QUANTITY,
}


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# --------------------- CREATES NEW USER ACCOUNT ------------------------
# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)


# --------------------- CREATES USER'S NEW GRAPH ------------------------

# response = requests.post(url= graph_endpoint, json= graph_params, headers= headers)
# print(response.text)


# --------------------- UPDATES USER'S GRAPH ------------------------

# response = requests.put(url= update_endpoint, json= update_params, headers= headers)
# print(response.text)


# --------------------- DELETES USER'S GRAPH ------------------------
#
# response = requests.delete(url= delete_endpoint, headers= headers)
# print(response.text)







