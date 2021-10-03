import os


class  Config:

    TEMPLATES_AUTO_RELOAD = True

    SECRET_KEY = "63f4ce6948a9d40a72191bb94b9c23fb"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    EMAIL_USER = os.getenv('EMAIL_USER')
    API_KEY = 'e0f45b48f51e45e54687c554e4b8dfe4'