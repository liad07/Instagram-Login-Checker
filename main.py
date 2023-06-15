import requests
from datetime import datetime


time = int(datetime.now().timestamp())
def IsExists(user,password):
  url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
  password=password

  payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
  'optIntoOneTap': 'false',
  'queryParams': {},
  'username': user}
  files=[

  ]
  headers = {

  }

  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  csrf=response.cookies["csrftoken"]
  headers = {
    'X-Csrftoken': f'{csrf}',
    'Cookie': f"csrftoken={csrf}; mid=ZIrEtgALAAE7GrCUwQ9wcQbbrefW; ig_did=80445D30-C9F9-4D3F-8BF0-78B39275775C; ig_nrcb=1; datr=tcSKZFMeDkyjVKNghYr_9-WI"
  }
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  return  (response.json())
user=input("enter user\n")
password=input("enter password\n")
x=IsExists(user,password)
if x["status"]=="ok" and x["authenticated"]!=None and x["authenticated"]==True:
  print("user and password matching ")
else:
  print("no password or user are correct")
  print(x)
