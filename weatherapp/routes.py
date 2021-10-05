
from logging import raiseExceptions
from requests import status_codes
from weatherapp import weather_app,requests,json,request
from flask import render_template,redirect,request,url_for,flash
from weatherapp.config import Config
from weatherapp.utils import get_current_location, get_metric,save_email,send_subscribe_confirm,save_email


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))




apiid = weather_app.config['WEATHER_API_KEY']
current_location = get_current_location()


@weather_app.route('/preferences',methods = ['GET','POST'])
def preferences():
    if request.method == 'POST':
        #get the metric option 
        option = request.form.get('temperature_preference')  
        return redirect(url_for('index',option=option))  
    pass




@weather_app.route("/", methods = ['GET','POST'])
def index():

    # option = request.args.get('option')

    # if option == None:
    #     unit = 'metric'
    # unit_name = get_metric(unit)


    city = current_location.get('city')
    if request.method == "POST":
        city = request.form.get('city')
        if city == "" or len(city) > 15:
            flash(f'Search field cannot be blank or more than 15 letters','danger')
            return redirect(url_for('index'))

    try:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'

        option = request.args.get('option')
        unit = 'metric'
        r = requests.get(url.format(city,apiid,unit))
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
        'icon': f'http://openweathermap.org/img/w/{icon_id}.png',
        # 'unit':unit_name 
        'unit':get_metric(option)    
        
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

    
    subscriber_name = request.form.get('subscriber-name')
    subscriber_email = request.form.get('subscriber-email')
    subscriber_name = subscriber_name.capitalize()
    
    try:
        save_email(subscriber_email)
    except:
        flash('Your email could not be saved. It may already exist','danger')

    else:
        send_subscribe_confirm(subscriber_name,subscriber_email)
        flash('You subscription has been completed successfully','info')
    return redirect(url_for('index'))
    
        
    
       
    # save_to_mailing_list()
       
    

    

