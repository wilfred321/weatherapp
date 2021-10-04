
from logging import raiseExceptions
from requests import status_codes
from weatherapp import weather_app,requests,json,request
from flask import render_template,redirect,request,url_for,flash
from weatherapp.config import Config
from weatherapp.utils import get_city_name


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))




apiid = weather_app.config['WEATHER_API_KEY']
current_city = get_city_name()

@weather_app.route("/", methods = ['GET','POST'])
def index():

    
    city = current_city
    if request.method == "POST":
        city = request.form.get('city')
        # if city == "" or len(city) > 15:
        #     flash(f'Search field cannot be blank or more than 15 letters','danger')
        #     return redirect(url_for('index')  
        # else:
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    try:
        r = requests.get(url.format(city,apiid))
        data = r.json()
    except:
        flash("The city you entered is incorrect or does not exist on our database, Please try again!")
        return redirect(url_for('index'))
            
    else:
        weather = {
            'city':data['name'],
        }
        flash(f"Your city is {weather.get('city')}",'info')
        return render_template('index.html',weather=weather)

        
              
              
                # flash(f'Your city is {weather}','info')         
        

       

        
      
            

         
            #  flash('success')
            


    # city = get_city_name()
    
    # 

    # 

    # data = r.json()


    # icon_id = data['weather'][0]['icon']
    # weather = {
    
    # 'city':data['name'],
    # 'temperature':data['main']['temp'],
    # 'description':data['weather'][0]['description'],
    
    # 'country':data['sys']['country'],
    # 'timezone':data['timezone'], 
    # 'icon': f'http://openweathermap.org/img/w/{icon_id}.png'      
    # } 

    # return render_template('index.html',title = 'index',weather = weather)




@weather_app.route("/register")
def register():
    return render_template('register.html',title = 'register')

@weather_app.route("/register")
def download():
    pass


@weather_app.route("/subscribe")
def subscribe():
    pass

