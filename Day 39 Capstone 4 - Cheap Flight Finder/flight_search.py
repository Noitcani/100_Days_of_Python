import requests
import datetime as dt
from dateutil.relativedelta import relativedelta
import json

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, KIWI_API_KEY, ORIGIN_IATA):
        self.EP = "https://tequila-api.kiwi.com/v2/search"

        self.headers = {
            "apikey": KIWI_API_KEY,
            "Content-Type": "application/json",
        }

        self.origin = ORIGIN_IATA

    def scan_city_code(self, city):
        scan_params = {
            "term": city
        }

        response = requests.get(url="https://tequila-api.kiwi.com/locations/query",
                                params=scan_params,
                                headers=self.headers)

        print(response.raise_for_status())
        print(response.status_code)
        if response.status_code == 200:
            print("City Code Scan Success!")
        else:
            print("City Code Scan Failed!")

        return response.json()["locations"][0]["code"]

    def scan_flights(self, destination):
        scan_params = {
            "fly_from": self.origin,
            "fly_to": destination,
            "date_from": dt.datetime.now().strftime("%d/%m/%Y"),
            "date_to": (dt.datetime.today() + relativedelta(months=6)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 15,
            "curr": "SGD",
            "max_stopovers": 0,
        }

        response = requests.get(url=self.EP, headers=self.headers, params=scan_params)
        print(response.raise_for_status())
        print(response.status_code)
        if response.status_code == 200:
            print("Flights Scan Success!")

        else:
            print("Flights Scan Failed!")

        return response.json()

