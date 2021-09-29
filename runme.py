from flask import Flask
from flask import redirect,url_for,render_template

weather_app = Flask(__name__)

@weather_app.route("/")
def index():
    return render_template('index.html',title = 'index')

@weather_app.route("/home")
def home():
    
    return "<h1>This is the home page!</h1> <a href = '/'>Return to Index</a>"



if __name__ == "__main__":
    weather_app.run()