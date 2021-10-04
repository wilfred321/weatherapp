from requests.exceptions import HTTPError
from weatherapp import json,requests,weather_app


token = weather_app.config['IP_INFO_KEY']

def get_city_name():
    url = f"http://ipinfo.io/json?token={token}"
    try:
        response = requests.get(url)
    except Exception:
            return "Error: Unable to execute request"
    else:
        data = response.json()
        city = data['region']
        return city



    


# def get_city_name():
#     url = "http://ipinfo.io/json"
#     try:
#         response = requests.get(url)
#     except Exception:
#         return "Error: Unable to execute request"
#     else:
#         data = response.json()
#         city_name = data['city']
#         return city_name



