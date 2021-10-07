
from logging import raiseExceptions
from requests import status_codes
from weatherapp import weather_app,requests,json,request,db,session
from flask import render_template,redirect,request,url_for,flash
from weatherapp.config import Config
from weatherapp.models import City
from weatherapp.utils import get_current_location, get_metric, get_weather, make_api_call,save_email,send_subscribe_confirm,save_email


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))




apiid = weather_app.config['WEATHER_API_KEY']
current_location = get_current_location()


@weather_app.route('/base',methods = ['POST','GET'])
def base():
    return render_template('base.html',title = 'Weatherapp')

@weather_app.route('/preferences',methods = ['GET','POST'])
def preferences():
    if request.method == 'POST':
        #get the metric option 
        option = request.form.get('temp_pref') 
        session['option'] = option
    return redirect(url_for('index'))  
    




@weather_app.route("/", methods = ['GET','POST'])
def index():
    # unit = request.args.get('option')
    unit = session.get('option','metric')
    city = current_location.get('city')
    if request.method == "POST":
        city = request.form.get('city')
        if city == "" or len(city) > 15:
            flash(f'Search field cannot be blank or more than 15 letters','danger')
            return redirect(url_for('index'))

    try:

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'

        # option = request.args.get('option')
        # unit = option
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
        'unit':get_metric(unit)    
        
    }
    
       
        return render_template('index.html',weather=weather,current_location = current_location)

@weather_app.route('/favorite-cities', methods = ['GET','POST'])
def fav_cities():
    cities = City.query.all()

    weather_data = []
    for city in cities:

        unit= 'metric'
        data = make_api_call(city.name,apiid,unit)
        icon_id = data['weather'][0]['icon']

        weather = get_weather(data,icon_id)
        weather_data.append(weather)
        
        
    return render_template('favorite_cities.html',weather_data=weather_data)
 
   
  




@weather_app.route("/add-favorite-city",methods = ['GET','POST'])
def add_city():

    if request.method !='POST':
         return render_template('add_city.html', title = "add city")
    else:
         
        city = request.form.get('city')
        
        #query the weather api with this new city
        unit = 'metric'

        #clean the user input
        if city == None or len(city) > 15:
            flash("Please enter a valid city name",'danger')
            return redirect(url_for('add_city'))
        else:

            try:    
                data = make_api_call(city,apiid,unit)
                icon_id = data['weather'][0]['icon']
            except KeyError as e:
                flash('Key error occured','danger')
                return redirect(url_for('add_city'))
            else:
                weather_data = get_weather(data,icon_id)
                # if db.query(city.id).filter(city.name == weather_data['city'],city.type==weather_data['city'].type):
                cities = City.query.all()

                if len(cities) == 4:
                    flash("List is full, Please delete a city to be able to add another!",'info')
                    return redirect(url_for("add_city"))
                else:

                    for city in cities:
                        if city.name == weather_data['city']:
                            flash("City already exist in your favorite cities list",'danger')
                            return redirect(url_for('add_city'))
                    else: 
                        
                        new_city_object = City(name = weather_data['city'])
                    # if new_city_object in City.query.filter_by(name = weather_data['city']):     
                        db.session.add(new_city_object)
                        db.session.commit()
                        flash("City has been added to your list",'success')
                        return redirect(url_for('fav_cities'))
            


        # return render_template('add_city.html', title = "add city",city=city_name)
        UserImage.query.filter(UserImage.user_id == 1).count()


@weather_app.route('/remove-city<string:city_id>', methods = ['GET','POST'])
def remove_city(city_id):
   city = City.query.filter_by(name = city_id).first()
   if city:
       db.session.delete(city)
       db.session.commit()
       flash(f'{city.name} was successfully deleted from your favorite cities','success')
       return redirect(url_for('fav_cities'))



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
       
    

    

