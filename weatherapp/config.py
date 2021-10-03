import os


class Config:

    TEMPLATES_AUTO_RELOAD = True
    FLASK_DEBUG = 1
    EMAIL_USER = os.getenv('EMAIL_USER')
    WEATHER_API_KEY = 'e0f45b48f51e45e54687c554e4b8dfe4'
    EXCHANGE_RATE_API_KEY = 'access_key=de93c2c03afac117dea9ca3eb291e4e5'
    SECRET_KEY = 'a4807791cc41a979d36f455b6e63ef5743aae26a57348334af566a1da52f81e3'

    #email config
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASS")