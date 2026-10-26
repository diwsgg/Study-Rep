import requests
from datetime import datetime, timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

#the path for the ENV
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)
API_KEY = os.getenv('Flight_APIKEY')
ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = ENDPOINT
        self.key = API_KEY
        self.engine = "google_flights"
        self.departure_id = "LHR"

    #this will be call for n times with the IATA Codes that we get from data_manager on main
    def transformParameters(self, code: str, number_stops):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_later  = datetime.now() + timedelta(days=6 * 30)
        params = {
            "api_key":self.key,
            "engine": self.engine,
            "departure_id":self.departure_id,
            "type": '1',
            "arrival_id": code,
            "outbound_date": tomorrow.strftime("%Y-%m-%d"),         
            "return_date":   six_month_later.strftime("%Y-%m-%d"),
        }
        #first create the params with all the data and then just if is none we can omit this 
        if number_stops is not None:
            params["stops"]= number_stops 

        return params
        
    def getFlightData(self, code : str, stops):
        #This makes it impossible to forget to prepare the parameters before making the request.
        params = self.transformParameters(code, stops)
        response = requests.get(self.url, params=params)
        data = response.json()
        if "error" in data:
            print("API error:", data["error"])
        else:
            #we are returing the value of data only
            return data
            

    