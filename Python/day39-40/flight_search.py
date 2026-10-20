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
        self.arrival_id = ''
        self.type = "1"
        self.params = {}
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.six_month_later  = datetime.now() + timedelta(days=6 * 30)

    #this will be call for n times with the IATA Codes that we get from data_manager on main
    def transformParameters(self, code: str):
        self.params = {
            "api_key":self.key,
            "engine": self.engine,
            "departure_id":self.departure_id,
            "type": self.type,
            "arrival_id": code,
            "outbound_date": self.tomorrow.strftime("%Y-%m-%d"),         
            "return_date":   self.six_month_later.strftime("%Y-%m-%d"),
        }
        #once are stored on params, we can getFlightData 
        # self.getFlightData()

    
    #not finished yet
    def comparePrices(self, data, price : str):
        flights = data.get("best_flights", []) + data.get("other_flights", [])
        cheapest = min(flights, key=lambda f: f["price"])
        print(f"Cheapest LHR-CDG: GBP {cheapest['price']}")
        return cheapest
        ...
        
    def getFlightData(self,price):
        response = requests.get(self.url, params=self.params)
        data = response.json()
        if "error" in data:
            print("API error:", data["error"])
        else:
            self.comparePrices(data,price)
            

    