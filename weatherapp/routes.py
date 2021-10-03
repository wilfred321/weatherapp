
from requests import status_codes
from weatherapp import weather_app,requests,json
from flask import render_template,redirect,request,url_for,flash
from weatherapp.config import Config


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))






@weather_app.route("/", methods = ['GET','POST'])
def index():

    apiid = weather_app.config['API_KEY']
    
    if request.method != 'POST':
        city = 'Lagos'
    else:  
        city = request.form.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    r = requests.get(url.format(city,apiid))
       
        # city = data['name']
    

   

#Get Weather for lagos


   
     
        

        # data = json.loads(r)
        # res = r.status_code
 

    data = r.json()
    icon_id = data['weather'][0]['icon']
    weather = {
        # 'city':city.capitalize(),
        'city':data['name'],
        'temperature':data['main']['temp'],
        'description':data['weather'][0]['description'],
        
        'country':data['sys']['country'],
        'timezone':data['timezone'], 
        'icon': f'http://openweathermap.org/img/w/{icon_id}.png'      
    } 

    return render_template('index.html',title = 'index',
    weather = weather)




@weather_app.route("/register")
def register():
    return render_template('register.html',title = 'register')
