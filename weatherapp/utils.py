from requests.exceptions import HTTPError
from weatherapp import socket,json,requests,request




def get_city_name():
    url = "http://ipinfo.io/json"
    try:
        response = requests.get(url)
    except Exception:
            return "Error: Unable to execute request"
    else:
        data = response.json()
        city_name = data['city']
        return city_name

    




