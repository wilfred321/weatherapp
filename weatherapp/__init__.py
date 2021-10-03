import requests, json, socket
from datetime import datetime
from flask import Flask, request
from logging import DEBUG
from weatherapp.config import Config
from email.message import EmailMessage

weather_app = Flask(__name__)
weather_app.config.from_object(Config)
weather_app.debug = 1

from weatherapp import routes