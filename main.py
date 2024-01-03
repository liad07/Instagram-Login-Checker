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
  mid=response.cookies["mid"]
  ig_did=response.cookies["ig_did"]
  ig_nrcb=response.cookies["ig_nrcb"]
  headers = {
    'X-Csrftoken': f'{csrf}',
    'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};"
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
