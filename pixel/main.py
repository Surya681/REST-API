import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
USERNAME="USERNAME"
TOKEN="YOUR_TOKEN"
graph_id="graph1"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":graph_id,
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":TOKEN,

}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_endpoint=f"{graph_endpoint}/{graph_id}"
today=datetime.now()
# pixel_config={
#     # "date":today.strftime("%Y%m%d"),
#     "date":"20220119",
#     "quantity":"10",
# }

# response=requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)

update_endpoint=f"{pixel_endpoint}/20220119"

# update_config={
#     "quantity":"1"
# }


response=requests.delete(url=update_endpoint,headers=headers)
print(response.text)