import os

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.

# data_manager - Get {list of countries: lowest price} in sheet

## ENV_KEYS to provide
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_EP = os.environ.get("SHEETY_EP")
ORIGIN_IATA = "SIN"

flight_search = FlightSearch(KIWI_API_KEY=KIWI_API_KEY, ORIGIN_IATA=ORIGIN_IATA)
sheety_manager = DataManager(SHEETY_EP=SHEETY_EP, SHEETY_AUTH=SHEETY_AUTH)

#######################

operation = input("Type 'Update Cities' or 'Scan' ").title()

if operation == "Update Cities":
    sheety_current_data = sheety_manager.get_rows()["flights"]
    sheety_city_dict = {row["id"]: row["city"] for row in sheety_current_data}

    for row, city in sheety_city_dict.items():
        citycode = flight_search.scan_city_code(city)
        cheapest_flight_scan = flight_search.scan_flights(citycode)
        cheapest_flight_data = FlightData(cheapest_flight_scan)
        cheapest_flight_structured_data = cheapest_flight_data.cheapest_flight_info()
        sheety_manager.write_to_sheety(row, cheapest_flight_structured_data)

elif operation == "Scan":
    sheety_current_data = sheety_manager.get_rows()["flights"]
    print(sheety_current_data)

    for city in sheety_current_data:
        citycode = flight_search.scan_city_code(city["cityCode"])
        cheapest_flight_scan = flight_search.scan_flights(citycode)
        cheapest_flight_data = FlightData(cheapest_flight_scan)
        cheapest_flight_structured_data = cheapest_flight_data.cheapest_flight_info()
        destination_city = cheapest_flight_structured_data["city"]
        destination_iata = cheapest_flight_structured_data["iataCode"]

        if cheapest_flight_structured_data["lowestPrice"] < city["lowestPrice"]:
            print(f"Hot Deal Found! Fly from {ORIGIN_IATA} to {destination_city}-{destination_iata} "
                  f"for {cheapest_flight_structured_data['lowestPrice']}, "
                  f"from {cheapest_flight_data.datefrom} to {cheapest_flight_data.dateto}")

        else:
            print("No Deals Found")




