from requests.exceptions import HTTPError
from weatherapp import json,requests




def get_city_name():
    url = "http://ipinfo.io/json"
    try:
        response = requests.get(url)
    except Exception:
            return "Error: Unable to execute request"
    else:
        data = response.json()
        city = data['city']
        return city

    




