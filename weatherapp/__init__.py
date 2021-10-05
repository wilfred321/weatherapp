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



db = SQLAlchemy()
mail = EmailMessage()

from weatherapp import routes

