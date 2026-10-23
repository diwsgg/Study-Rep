import requests
from pathlib import Path
import os
from dotenv import load_dotenv

#the path for the ENV
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)
API_KEY_SHEETY = os.getenv('AUTHORIZATION_FLIGHTSheety')
ENDPOINT_SHEETY = "https://api.sheety.co/56df9d1d9fe8908c5a3bcfe5d729cf6b/iataCodes/prices"
HEADER_SHEETY={
    'authorization':API_KEY_SHEETY,
}

#This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.url = ENDPOINT_SHEETY
        self.header = HEADER_SHEETY
        #initialize it with data
        self.data_sheety=self.getData()

    def getData(self):
        response_sheety = requests.get(url=self.url, headers=self.header)
        response_sheety.raise_for_status()
        self.data_sheety = response_sheety.json()
        return self.data_sheety

    #we can update the data of the sheet after we have check if some flight price is lower that current one
    def PutData(self, id, new_price):
        post_url = self.url+'/'+id

        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }

        response_sheety = requests.put(url=post_url, json=new_data, headers=self.header)
        response_sheety.raise_for_status()
        print(f"Updated price for {id}")



    #we are not posting since we are only comparing the ones that we have, but 
    #we can implement this after, with a menu of options, 