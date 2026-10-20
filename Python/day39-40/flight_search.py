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
    def transformParameters(self, code: str):
        tomorrow = datetime.now() + timedelta(days=1)
        six_month_later  = datetime.now() + timedelta(days=6 * 30)
        #the change for that making local variables
        #is that we can change those values in the interactions that we will do
        params = {
            "api_key":self.key,
            "engine": self.engine,
            "departure_id":self.departure_id,
            "type": '1',
            "arrival_id": code,
            "outbound_date": tomorrow.strftime("%Y-%m-%d"),         
            "return_date":   six_month_later.strftime("%Y-%m-%d"),
        }
        return params

    
    #not finished yet
    def comparePrices(self, data, price : float):
        flights = data.get("best_flights", []) + data.get("other_flights", [])
        cheapest = min(flights, key=lambda f: f["price"])
        #Once we have the chepeast
        if cheapest<price:
            #then is a deal
            #we have to return cheapest
            return cheapest
        return None
        
    def getFlightData(self, code : str, price: float):
        #This makes it impossible to forget to prepare the parameters before making the request.
        params = self.transformParameters(code)
        response = requests.get(self.url, params=params)
        data = response.json()
        if "error" in data:
            print("API error:", data["error"])
        else:
            self.comparePrices(data,price)
            

    