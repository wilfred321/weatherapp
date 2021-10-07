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

# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# # print(IPAddr)
# # print(hostname)

# query = IPAddr
# fields = [
#     "status",
#     "message",
#     "country",
#     "countryCode"
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
# print(data)

# response = requests.get(url)
# print(response.status_code)

# import re
# import json
# import urlopen

# url = "http://ipinfo.io/json"
# response = urlopen(url)
# data = json.load(response)

# ip = data["ip"]
# org = data["org"]
# city = data["city"]

# print(ip)
# print(org)
# print(city)

# import requests
# def get_city_name():
#     url = "http://ipinfo.io/json"
#     try:
#         response = requests.get(url)
#     except Exception:
#             return "Error: Unable to execute request"
#     else:
#         data = response.json()
#         return data
        
# print(get_city_name())





# print(get_city_name())

# fullname = 'Wilfred Owobu'
# _,lastname = fullname.('/')
# print(lastname)

# def get_metric(unit= 'metric'):
#     switcher = {
#         'metric':'Celcius ',
#         'standard':'Kelvin',
#         'imperial':'Farenheit',
#     }  

#     return switcher.get(unit,'metric')

# print(get_metric())
# from os import abort


# email = 'wiasfdlffk@asfdlfkj.com'

# def save_email(email):

#     with open('..\mailing_list.txt','r+') as f:
#         file = f.read()
#         if email not in file:
#             f.write(email)
#             f.write('\n')
           
        

# save_email(email)


# def greet(name):
#     print( f"Hello {name}")

# greet('wilfred')


# import os
# import requests
# import json
# r = requests.get('http://api.ipify.org')



# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
# print(IPAddr)
# print(hostname)
# IPAddr = r.text
# query = IPAddr
# fields = [
    
#     "countryCode"
#     "region",
   
#     "city",
    
   
# ]

# url = f"http://ip-api.com/json/{query}?={fields}"

# r = requests.get(url)
# data = r.json()
# print(data['org'])
# print(data['country'])
# print(data['countryCode'])
# print(data['city'])



# from pathlib import Path
# import requests
# url = Path('/test/flask_blog.pdf')
# # url = Path('/test')
# # response = requests.get(url)
# # response.write_bytes(response.content)
# file = open(url,'wb')
# print(file.write)

# import os
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template

# template = Template(Path('template.html').read_text())
# # template.substitute()



# EMAIL_USER = os.getenv('EMAIL_USER')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

# message = MIMEMultipart()
# message['from'] = EMAIL_USER
# message['to'] = 'owobuwilfred@gmail.com'
# message['subject'] = 'This is a test!'
# body = template.substitute({'name':'john'})
# message.attach(MIMEText(body,"html"))
# message.attach(MIMEImage(Path("profile_pic.jpeg").read_bytes()))


# with smtplib.SMTP(host = 'smtp.gmail.com',port = 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login(EMAIL_USER,EMAIL_PASSWORD)
#     smtp.send_message(message)
#     print("SENT...")


# def get_metric(option):
#     switcher = {
#          'metric':'Celcius ',
#          'standard':'Kelvin',
#          'imperial':'Farenheit',
#     }  

#     return switcher.get(option,'metric')
option = None
unit = option if option !=None else option
print(unit)

