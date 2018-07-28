import os
from flask import Flask, request, render_template
import requests
from urllib import parse
from .constants import API_KEY,API_URL

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/weather/india', methods=['GET'])
    def my_form_post():
        city = request.args.get('city')
        city_country = city + ',in'
        print('City: %s Country: %s'%(city,'India'))
        payload = {
            'q' : city_country,
            'APPID': API_KEY,
            'mode': 'html',
            'units': 'metric'
        }
        try:
            req = requests.get(API_URL, params=payload)
            # return req.text
            html_string = req.text.replace('\"','\'')
            return render_template('result.html',result=html_string)
        except Exception as e:
            print(e)
            return "<h1>Error 404 Not found</h1>"
        
    return app