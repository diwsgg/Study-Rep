class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure, arrival, price, outbound_date, return_date, stops):
        self.departure = departure
        self.arrival = arrival
        self.price = price
        self.outbound_date = outbound_date
        self.return_date = return_date
        self.stops = stops