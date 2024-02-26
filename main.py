from pprint import pprint
import os

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = 'eab14b134c19ebda9ad67fa887f2e4fe'

@app.route('/')
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
