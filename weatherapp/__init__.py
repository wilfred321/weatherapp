import json,requests,socket
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

from logging import DEBUG
from weatherapp.config import Config

from email.message import EmailMessage
import smtplib

weather_app = Flask(__name__)
weather_app.config.from_object(Config)
weather_app.debug = 1


#Application context




db = SQLAlchemy()
mail = EmailMessage()

db.init_app(weather_app)
with weather_app.app_context():
    db.create_all()

from weatherapp import routes

