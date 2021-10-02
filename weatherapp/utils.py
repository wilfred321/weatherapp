from requests.exceptions import HTTPError
from weatherapp import socket,json,requests,request



# def get_city_name():
    # hostname = socket.gethostname()
    # IPAddr = socket.gethostbyname(hostname)
    # IPAddr = '197.210.8.76'
    # query = IPAddr
    # fields = ['city']
    # url = f"http://ip-api.com/json/{query}?={fields}"
    # r = requests.get(url)
    # data = r.json()
    # city = data['city']
    # return city
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

    




