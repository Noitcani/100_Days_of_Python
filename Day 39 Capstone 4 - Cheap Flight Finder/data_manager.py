import requests

class DataManager:
    def __init__(self, SHEETY_EP, SHEETY_AUTH):
        self.EP = SHEETY_EP

        self.headers = {
            "Authorization": SHEETY_AUTH,
            "Content-Type": "application/json"
        }

    def get_rows(self):
        response = requests.get(url=self.EP, headers=self.headers)
        print(response.raise_for_status())
        print(response.status_code)
        if response.status_code == 200:
            print("Sheet Info Pull Success!")
        else:
            print("Sheet Info Pull Failed!")

        return response.json()

    def write_to_sheety(self, row, structured_info):
        sheety_params = {
            "flight": {
                "city": structured_info["city"],
                "cityCode": structured_info["cityCode"],
                "iataCode": structured_info["iataCode"],
                "lowestPrice": structured_info["lowestPrice"],
            }
        }

        response = requests.put(url=f"{self.EP}/{row}", json=sheety_params, headers=self.headers)
        print(response.raise_for_status())
        print(response.status_code)
        if response.status_code == 200:
            print("Sheety Update Success!")
        else:
            print("Sheety Update Failed!")

