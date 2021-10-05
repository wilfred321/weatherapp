
from logging import raiseExceptions
from requests import status_codes
from weatherapp import weather_app,requests,json,request
from flask import render_template,redirect,request,url_for,flash
from weatherapp.config import Config
from weatherapp.utils import get_current_location,send_subscribe_confirm


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))




apiid = weather_app.config['WEATHER_API_KEY']
units = get_metric()
current_location = get_current_location()

@weather_app.route("/", methods = ['GET','POST'])
def index():

    
    city = current_location.get('city')
    if request.method == "POST":
        city = request.form.get('city')
        if city == "" or len(city) > 15:
            flash(f'Search field cannot be blank or more than 15 letters','danger')
            return redirect(url_for('index'))

    try:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        r = requests.get(url.format(city,apiid,))
        data = r.json()
        city = data['name']
    except:
        flash("The city you entered is incorrect or does not exist on our database, Please try again!",'danger')
        return redirect(url_for('index'))
        
    else:

        icon_id = data['weather'][0]['icon']
        weather = {
        'city':data['name'],
        'temperature':data['main']['temp'],
        'description':data['weather'][0]['description'],
        
        'country':data['sys']['country'],
        'timezone':data['timezone'], 
        'icon': f'http://openweathermap.org/img/w/{icon_id}.png'      
        
    }

    return render_template('index.html',weather=weather, current_location = current_location)

        
   
  




@weather_app.route("/register")
def register():
    return render_template('register.html',title = 'register')

@weather_app.route("/register")
def download():
    pass


@weather_app.route("/subscribe", methods = ['GET','POST'])
def subscribe():

    
    subscriber_username = request.form.get('subscriber-username')
    subscriber_email = request.form.get('subscriber-email')
    firstname,lastname = subscriber_username.capitalize().split(' ')
    
    send_subscribe_confirm(firstname,subscriber_email)
    # save_to_mailing_list()
    flash('You subscription has been completed successfully','info')
    return redirect(url_for('index'))
    

    

