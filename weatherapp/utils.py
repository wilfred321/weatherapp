from email.message import EmailMessage
import smtplib
from requests.exceptions import HTTPError
from weatherapp import socket, json, requests, request, datetime, weather_app
import weatherapp


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


def get_unit(option):

    switcher = {
        'metric': ' Celcius',
        'standard': 'Kelvin',
        'imperial': 'Farenheit'
    }
    return switcher.get(option, "metric")


def get_current_datetime():
    return datetime.utcnow()


#LOGIN TO MAIL SERVER

SENDER = weather_app.config['MAIL_USERNAME']
EMAIL_PASSWORD = weather_app.config['MAIL_PASSWORD']

smtp = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
try:
    smtp.login(SENDER, EMAIL_PASSWORD)
except:
    print('Error logging in to the mail server')
else:
    print('User logged in successfully')


#CREATE MAILING LIST
def send_subscription_notification(fullname, email):
    msg = EmailMessage()
    msg['From'] = SENDER
    msg['To'] = email
    msg['Subject'] = 'Thank you for your subscription'
    msg.set_content(
        f"Dear {fullname}\n\n Thank you for subscribing to receive notification from us. \n\n\n Regards \n From WeatherApp"
    )
    smtp.send_message(msg)