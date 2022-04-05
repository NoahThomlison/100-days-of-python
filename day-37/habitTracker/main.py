import requests
from datetime import datetime

pixelaEndPoint = "https://pixe.la/v1/users"
USERNAME = "noahthomlison1"
TOKEN = "noahsT123123124124515415123123okenforPixela123"
GRAPH_ID = "abc123"

user_params = {
  "token":TOKEN, 
  "username":USERNAME, 
  "agreeTermsOfService":"yes", 
  "notMinor":"yes"
}

# response = requests.post(url=pixelaEndPoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixelaEndPoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create end point
pixel_creation_endpoint = f"{pixelaEndPoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

# update endpoint
new_pixel_data = {
    "quantity": "10"
}
update_endpoint = f"{pixelaEndPoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{pixelaEndPoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
