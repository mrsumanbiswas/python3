"""
## This to ease out the process of finding available slots of vaccination centre by using simple python script.\n
### ```It just need an active internet connection and a valid pincode/zipcode.```
@author: ``mrsumanbiswas``\n
Date: ``06-01-2022``\n
``Github``: https://github.com/mrsumanbiswas\n
``Linkedin``: https://www.linkedin.com/in/mrsumanbiswas\n
# Thanks for visiting.
"""
###############################
#######     IMPORTS     #######
###############################
import os
import json
import requests
from time import strftime
##############################
#########     CODE    ########
##############################
Continue = True
while Continue:
    pincode = input("The the pincode/zipcode of nearest vacination center : ")
    if len(pincode) == 6:
        Continue = False
    else:
        os.system('clear')
        print("Please Enter a valid pincode/zipcode.")
def main(response):
    with open(f'{os.getcwd()}/response.json','w+') as f:
        f.write(response)
    with open(f"{os.getcwd()}/response.json",'r') as f:
        response : dict = json.loads(f.read(),)
    response:list = response['sessions']
    if response != []:
        data = ""
        for i in range(len(response)):
            for key in response[i]:
                value = response[i][f'{key}']
                data += f"""{key.replace('_',' ')} -> {value}\n\n"""
        if data != "":
            print(data)
        else:
            os.system(f'rm -r {os.getcwd()}/data')
            print(f"Sorry! no data avalable for {pincode} this area :-( ")
try:
    api_request = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={strftime('%d-%m-%Y')}" + "accept: application/json" + "Accept-Language: en_US"
    response = requests.get(url=api_request).text
    main(response)
except Exception as e:
    print("Sorry! Error: ",e)
##############################
########     THANKS    #######
##############################
