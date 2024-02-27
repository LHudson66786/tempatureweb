from pprint import pprint
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
load_dotenv()
api_key = os.environ.get('WEATHER_API_KEY')

@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/weather')
def weather():
    location = request.args.get('location')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    pprint(response)
    temperature = response['main']['temp']
    return f'The temperature in {location} is {temperature} degrees Celsius.'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
