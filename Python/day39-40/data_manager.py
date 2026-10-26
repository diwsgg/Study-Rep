import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import datetime
#the path for the ENV
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)
API_KEY_SHEETY = os.getenv('AUTHORIZATION_FLIGHTSheety')
ENDPOINT_SHEETY = "https://api.sheety.co/56df9d1d9fe8908c5a3bcfe5d729cf6b/iataCodes/"
HEADER_SHEETY={
    'authorization':API_KEY_SHEETY,
}

#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.url = ENDPOINT_SHEETY
        self.header = HEADER_SHEETY
        #initialize it with data
        self.data_sheety =self.getData()
        self.data_users = self.getUsersData()

    def getData(self):
        response_sheety = requests.get(url=(self.url+'prices'), headers=self.header)
        response_sheety.raise_for_status()
        self.data_sheety = response_sheety.json()
        return self.data_sheety

    def getUsersData(self):
        response_sheety = requests.get(url=(self.url+'users'), headers=self.header)
        response_sheety.raise_for_status()
        self.data_users = response_sheety.json()
        return self.data_users

    #we can update the data of the sheet after we have check if some flight price is lower that current one
    def PutData(self,id, new_price,final_link='prices'):
        put_url = self.url+final_link+'/'+id

        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }

        response_sheety = requests.put(url=put_url, json=new_data, headers=self.header)
        response_sheety.raise_for_status()
        print(f"Updated price for {id}")

    #we will use post for the users (name, and emails)
    def PostUserData(self, user_name, user_last_name, user_email):
        post_url = self.url+'users'
        time= datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        #the id is equal to our data lenght plus 2 
        id = len(self.data_users['users'])+2
        data_sent={
            'user':{
                'timestamp': time, 
                'whatIsYourFirstName?': user_name, 
                'whatIsYourLastName?': user_last_name, 
                'whatIsYouEmail?': user_email, 
                'id': id
            }
        }

        response_sheety = requests.post(url=post_url, json=data_sent, headers=self.header)
        response_sheety.raise_for_status()
        print(f"Created new user in row: {id}")