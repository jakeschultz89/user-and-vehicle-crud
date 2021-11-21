from pprint import pprint
import requests

TEST_VEHICLE_DATA = {
    "license_plate": "7777777",
    "v_type": "sedan",
    "color": "Purple",
    "parking_spot_no": 3,
    "description": "Grocery getter",
    "user_id": "1"
}

URL = 'http://127.0.0.1:5000/vehicles/1'

def update_vehicle():
    out = requests.put(URL, json=TEST_VEHICLE_DATA)
    if out.status_code == 200:
        pprint(out.json())
    else:
        print("Something went wrong while trying to update")


if __name__ == "__main__":
    update_vehicle()