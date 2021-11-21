from pprint import pprint
import requests

TEST_VEHICLE = {
    "license_plate": "59888DV",
    "v_type": "F250",
    "color": "Silver",
    "parking_spot_no": 1,
    "description": "Diesel F250 4X4",
    "user_id": 1
}

URL = "http://127.0.0.1:5000/vehicles"

def test_vehicle_creation():
    out = requests.post(URL, json=TEST_VEHICLE)
    if out.status_code == 201:
        out_json = out.json()
        pprint(out_json)
        return out_json["new_id"]
    else:
        print("Something went wrong while creating a vehicle.")
        return -1
        
if __name__ == "__main__": #calls whatever is listed below to run
    new_id = test_vehicle_creation()
