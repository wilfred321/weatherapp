
from requests import status_codes
from weatherapp import weather_app,requests,json
from flask import render_template,redirect,request,url_for
from weatherapp.config import Config


# @weather_app.route("/search", methods = ['GET','POST'])
# def search():
    
#     city = request.form.get('city')
    

#     return redirect(url_for('index',city_name = city))






@weather_app.route("/", methods = ['GET','POST'])
def index():

    apiid = weather_app.config['API_KEY']
    try:
        
        city_name = request.form.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apiid}'

        r = requests.get(url)
        data = r.json()
        city = data['name']
        
    except:

         message = 'Invalid City Selected'
         return render_template('index.html', message = message)   
   

#Get Weather for lagos


   
     
        

        # data = json.loads(r)
        # res = r.status_code
    else:
        country = data['sys']['country']
        clouds = data['clouds']['all']
        # weather_val = data['weather']['main']
        temperature = data['main']['temp']
        code = data['cod']
        return render_template('index.html',title = 'index',
        city = city,country=country, cloud = clouds ,temperature = temperature)




@weather_app.route("/register")
def register():
    return render_template('register.html',title = 'register')
