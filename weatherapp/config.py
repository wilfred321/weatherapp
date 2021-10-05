import os


class  Config:

    TEMPLATES_AUTO_RELOAD = True

    SECRET_KEY = "63f4ce6948a9d40a72191bb94b9c23fb"

    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    WEATHER_API_KEY = 'e0f45b48f51e45e54687c554e4b8dfe4'
    IP_INFO_KEY = 'c11082615e5035'


    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASS = os.getenv('EMAIL_PASS')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True

