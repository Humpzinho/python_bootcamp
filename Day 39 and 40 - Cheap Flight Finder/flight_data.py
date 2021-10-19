class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, cityFrom, airportFrom, cityTo, airportTo,
                 outDate, returnDate, link,stop_overs=0, via_city=""):
        self.price = price
        self.cityFrom = cityFrom
        self.airportFrom = airportFrom
        self.cityTo = cityTo
        self.airportTo = airportTo
        self.outDate = outDate
        self.returnDate = returnDate
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.link = link