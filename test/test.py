# import os
# import smtplib
# from email.message import EmailMessage
# import imghdr

# msg = EmailMessage()

# EMAIL_ADDRESS = os.getenv("EMAIL_USER")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
# EMAIL_RECIPENT = "owobuwilfred@gmail.com"

# msg["Subject"] = "Sending HTML Message"
# msg["From"] = EMAIL_ADDRESS
# msg["To"] = EMAIL_RECIPENT
# msg.set_content("This is a plain text email")
# name = "Wilfred"
# html = """\
# <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">

#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>

#     <style>
#         body {
#             background-color: green;
#         }

#         .btn {
#             height: 50px;
#             border: solid blue 1px;
#             font-family: Arial, Helvetica, sans-serif;
#             font-size: large;
#             margin: auto;
#         }
#     </style>
# </head>

# <body>
#     <h1 style="color:grey">This is a simple HTML</h1>

#     <div class='form-group'>
#         <button class='btn'>Download Whitepaper</button>
#     </div>
# </body>

# </html>
#     """
# msg.add_alternative(html, subtype="html")

# files = ["flask_blog.pdf"]

# for file in files:
#     with open(file, "rb") as f:
#         file_data = f.read()
#         # file_type = imghdr.what(f.name)
#         file_name = f.name
#     msg.add_attachment(
#         file_data, maintype="application", subtype="octet-stream", filename=file_name
#     )

# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.send_message(msg)
#         print("Your message has been sent successfully")
# except:
#     print("Sorry, Unable to send message!")

# from flask_blog.models import User,Post
# from flask_blog import db
# import json
# # users = User.query.all()
# # for user in users:
# #     print(user.username)
# # posts = Post.query.all()
# # for post in posts:
# #     print(post )
# with open('post1.json') as file:
#     data = json.load(file)
#     for post in data:
#         posts =  Post(title = post['title'], content = post['content'],user_id = post['user_id'])
#         db.session.add(posts)
#         db.session.commit()
# data = json.dumps(file)
# print(type(data))
# print(post.user_id)
# posts = Post.query.all()
# index = 1
# for post in posts:
#     print( f' {index}. Post title: {post.title}\n Post Content: {post.content}')
#     index += 1

# import socket
# import requests
# import json

# # hostname = socket.gethostname()
# # IPAddr = socket.gethostbyname(hostname)
# # print(IPAddr)
# # print(hostname)
# IPAddr = '197.210.8.76'
# query = IPAddr
# fields = [
#     "status",
#     "message",
#     "country",
#     "countryCode",
#     "region",
#     "regionName",
#     "city",
#     "zip",
#     "lat",
#     "lon",
#     "timezone",
#     "isp",
#     "org",
#     "as",
#     "query",
# ]

# url = f"http://ip-api.com/json/{query}?={fields}"

# r = requests.get(url)
# data = r.json()
# print(type(data))
# # print(data)
# city = data['city']
# print(city,)

# for key, value in enumerate(data):
#     print(f"{key} = {data}")

# response = requests.get(url)
# print(response.status_code)

# import requests
# import json

# url = "http://ipinfo.io/json"
# response = requests.get(url)
# data = response.json()

# ip = data["ip"]
# org = data["org"]
# city = data["city"]

# print(ip)
# print(org)
# # print(city)
# from enum import IntEnum
# from logging import raiseExceptions

# import requests
# from requests import HTTPError
# import json
# city_name = "Lagos"
# api_id = 'e0f45b48f51e45e54687c554e4b8dfe4'
# unit = 'metric'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_id}&units={unit}'

# r = requests.get(url)
# data = r.json()
# humidity = data['main']['humidity']
# weather = data['weather']
# print(type(weather))
# # print(type(weather))
# # print(weather)
# # result = [x.items for x in weather]
# # print(result)

# weather_dict = weather[0]
# # for key,value in weather_dict.items():
# #     print(f'{key}:{value}')
# print(weather_dict['description'])
# print(weather_dict['main'])
# print(weather_dict['id'])

# from re import A
# import secrets

# SK = secrets.token_hex()
# print(SK)

# def unit(i):
#     switcher = {
#         : 'Sunday',
#         1: 'Monday',
#         2: 'Tuesday',
#         3: 'Wednesday',
#         4: 'Thursday',
#         5: 'Friday',
#         6: 'Saturday'
#     }
#     return switcher.get(i, "Invalid day of week")

# print(week(0))

# def get_unit(option):

#     switcher = {
#         'metric': ' &#8451',
#         'standard': '&#8490',
#         'imperial': '&#8457'
#     }
#     return switcher.get(option, "metric")

# weather_data = json.dum
# ps(weather)
# print(type(weather_data))

# print(weather[0])
# except ImportError:
#     print("Import Error: One or more imports failed")
# else:
#     def get_city_name():
#         url = "http://ipinfo.io/json"
#         try:
#             response = requests.get(url)
#         except Exception:
#             raiseExceptions
#             print("Error: Unable to execute request")
#         else:
#             data = response.json()
#             city_name = data['city']
#             return city_name

# print((get_city_name()))

name = 'wilfred'
email = 'demo@demo.comm'

with open('mlist.txt', 'r+') as f:
    file = f.read()
    if email in file:
        print("sorry, email already exist in our mailing list")
    else:
        f.write(email)
        f.write('\n')
        print(f"{email} has been saved")
