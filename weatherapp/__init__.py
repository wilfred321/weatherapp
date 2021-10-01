import requests,json
from flask import Flask
from logging import DEBUG
from weatherapp.config import Config

weather_app = Flask(__name__)
weather_app.config.from_object(Config)

from weatherapp import routes