from flask import Flask
from flask import redirect,url_for

weather_app = Flask(__name__)

@weather_app.route("/")
def index():
    return "<h1>Hello , Universe!</h1>"

@weather_app.route("/home")
def home():
    
    return "<h1>This is the home page!</h1> <a href = '/'>Return to Index</a>"



if __name__ == "__main__":
    weather_app.run()