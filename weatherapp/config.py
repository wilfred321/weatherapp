import os


class  Config:

    TEMPLATES_AUTO_RELOAD = True
    FLASK_DEBUG = 1
    EMAIL_USER = os.getenv('EMAIL_USER')
    API_KEY = 'e0f45b48f51e45e54687c554e4b8dfe4'