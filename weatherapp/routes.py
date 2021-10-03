from logging import raiseExceptions
from weatherapp import weather_app, requests, json
from flask import render_template, redirect, request, url_for, session, flash, get_flashed_messages
from weatherapp.config import Config

from weatherapp.utils import get_city_name, get_current_datetime, get_unit, send_subscription_notification

# @weather_app.route("/search", methods = ['GET','POST'])
# def search():

#     city = request.form.get('city')

#     return redirect(url_for('index',city_name = city))
apiid = weather_app.config['WEATHER_API_KEY']
apiid2 = weather_app.config['EXCHANGE_RATE_API_KEY']

current_datetime = get_current_datetime()


@weather_app.route("/preferences", methods=['GET', 'POST'])
def preferences():

    option = request.form.get('options')
    session['unit'] = option
    # return render_template('preferences.html', option=option)
    return redirect(url_for('index'))


# return redirect(url_for('index', unit=unit))

current_city = get_city_name()


@weather_app.route("/", methods=['GET', 'POST'])
def index():

    #get the metric data
    option = session.get('unit', None)
    # option = request.args.get('option')

    #get the hourly_focast_data
    # exchange_rate_data = request.args.get('exchange_rate_data')
    base_currency = request.args.get('base_currency')
    rates = request.args.get('rates')
    currency = request.args.get('currency')

    if option == None:
        unit = 'metric'

    else:
        unit = option
    unit_symbol = (get_unit(unit))
    # unit_symbol = raw_symbol.encode('ascii')
    try:

        city_name = request.form.get('city')
        if city_name == None:
            city_name = current_city

        try:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apiid}&units={unit}'
        except Exception:
            return "Error: Unable to execute request"
        r = requests.get(url)
        data = r.json()
        city = data['name']

    except:
        flash('Invalid city selected', 'danger')

        return redirect(url_for('index'))


#Get Weather for lagos

# data = json.loads(r)
# res = r.status_code
    else:
        country = data['sys']['country']
        clouds = data['clouds']['all']

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        code = data['cod']

        weather = data['weather']
        weather_dict = weather[0]
        description = weather_dict['description']
        icon = weather_dict['icon']
        return render_template('index.html',
                               title='index',
                               city=city,
                               country=country,
                               current_city=current_city,
                               temperature=temperature,
                               humidity=humidity,
                               description=description,
                               unit=unit,
                               unit_symbol=unit_symbol,
                               current_datetime=current_datetime,
                               base_currency=base_currency,
                               rates=rates,
                               currency=currency)

exchange_rate_url = 'http://data.fixer.io/api/latest?'


@weather_app.route("/exchange-rate", methods=['GET', 'POST'])
def exchange_rate():
    if request.method == 'GET':
        return "This method is not supported"
    else:

        currency = request.form.get('currency')
        if not currency:
            currency = 'USD'
        endpoint = exchange_rate_url + apiid2
        exchange_rate_response = requests.get(endpoint)
        exchange_rate_data = exchange_rate_response.json()

        base_currency = exchange_rate_data['base']

        # currency = 'USD'

        rate = exchange_rate_data['rates'][currency]
        rates = rate
        return redirect(
            url_for('index',
                    exchange_rate_data=exchange_rate_data,
                    base_currency=base_currency,
                    rates=rates,
                    currency=currency))


# @weather_app.route('/test', methods=['GET', 'POST'])
# def test():
#     name = request.args.get('name')
#     email = request.args.get('email')
#     return render_template('preferences.html', name=name, email=email)


@weather_app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if not request.method == 'POST':
        print("Request method must be a post")
    else:
        name = request.form.get('subscriber-name')
        email = request.form.get('subscriber-email')
        with open('mailing_list.txt', 'r+') as f:
            file = f.read()
            if email in file:
                flash("Sorry, your email already exist in our mailing list",
                      'danger')

            else:
                f.write(email)
                f.write('\n')
                send_subscription_notification(name, email)
                flash(
                    'A confirmation notification has been sent to your email',
                    'success')
                return redirect(url_for('index'))


@weather_app.route('/test-flash', methods=['GET', 'POST'])
def test_flash():
    # message = ' It is working'
    # flash(message)
    return render_template('preferences.html')
