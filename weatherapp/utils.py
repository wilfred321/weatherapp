from requests.exceptions import HTTPError
from weatherapp import json,requests,weather_app,mail,smtplib


token = weather_app.config['IP_INFO_KEY']

def get_current_location():
    url = f"http://ipinfo.io/json?token={token}"
    try:
        response = requests.get(url)
    except Exception:
            return "Error: Unable to execute request"
    else:
        data = response.json()

        location = {
            'city':data['region'],
            'country':data['country']
            }

        return location




email_username = weather_app.config['EMAIL_USER']

def connect_mail_server():
    email_server = weather_app.config['MAIL_SERVER']
    email_password = weather_app.config['EMAIL_PASS']
    email_port = weather_app.config['MAIL_PORT']
    try:
        smtp = smtplib.SMTP_SSL(email_server,email_port)
        smtp.login(email_username,email_password)
    except:
        print("Unable to establish connection to server")
    else:
        print("Successfully logged in to email server")
        return smtp



def send_subscribe_confirm(username,email):
    #create message
   
   
    mail['Subject'] = "WeatherApp - Thank you for joining mailing list"
    mail['From'] = email_username
    mail['To'] = email
    mail.set_content(f"Hi {username} \n\n Thank you for subscribing to our Weather Notification Service. \n Your email has been added to our mailing list \n\n\n With Best Regards \n WeatherApp Team")
    
    #establish connection to email server and send message
    smtp = connect_mail_server()
    smtp.send_message(mail)
        
def save_email(email):

    with open('mailing_list.txt','r+') as f:
        file = f.read()
        if email not in file:
            f.write(email)
            f.write('\n') 
        else:
            print("email already exists")

            
            
            

         
def get_metric(option):
    switcher = {
         'metric':'Celcius ',
         'standard':'Kelvin',
         'imperial':'Farenheit',
    }  

    return switcher.get(option,'metric')



def get_weather(data,icon_id):
   
    weather = {
   
    'city':data['name'],
    'temperature':data['main']['temp'],
    'description':data['weather'][0]['description'],
    'icon': f'http://openweathermap.org/img/w/{icon_id}.png',
    'country':data['sys']['country']  
    }
    return weather

def make_api_call(city,apiid,unit):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'
       
        r=requests.get(url.format(city,apiid,unit))
        data = r.json()
    except:
        print("api call not successful")
    else:
        return data


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



