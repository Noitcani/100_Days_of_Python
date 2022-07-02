import datetime as dt

class FlightData:
    def __init__(self, data):
        self.lowest_price = 0

        for i in range(len(data["data"])):
            if self.lowest_price == 0:
                self.lowest_price = data["data"][i]["price"]

            elif data["data"][i]["price"] < self.lowest_price:
                self.lowest_price = data["data"][i]["price"]
                self.cheapest_flight_index = i

        self.cheapest_flight = data["data"][self.cheapest_flight_index]
        self.city = self.cheapest_flight["cityTo"]
        self.cityCode = self.cheapest_flight["cityCodeTo"]
        self.iataCode = self.cheapest_flight["flyTo"]
        self.java_datefrom = self.cheapest_flight["route"][0]["local_departure"]
        self.java_dateto = self.cheapest_flight["route"][-1]["local_departure"]
        self.datefrom = dt.datetime.strptime(self.java_datefrom.split("T")[0], "%Y-%m-%d").strftime("%d/%m/%Y")
        self.dateto = dt.datetime.strptime(self.java_dateto.split("T")[0], "%Y-%m-%d").strftime("%d/%m/%Y")

    def cheapest_flight_info(self):
        structured_info = {
            "city": self.city,
            "cityCode": self.cityCode,
            "iataCode": self.iataCode,
            "lowestPrice": self.lowest_price,
        }

        return structured_info
