from flask import Flask

weather_app = Flask(__name__)

@weather_app.route("/")
def index():
    return "<h1>Hello , Universe!</h1>"



if __name__ == "__main__":
    weather_app.run()