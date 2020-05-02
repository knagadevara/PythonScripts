#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sat May  2 20:33:04 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import os, sys, argparse, requests , json
from time import strftime, localtime

parseme = argparse.ArgumentParser(prog='ShoWeather' , description= 'Shows Whether of the required country and zipcode' )
parseme.add_argument('--zipcode' , '-z' , type = int , required = True , help = ' - z <zipcode>')
parseme.add_argument('--country' , '-c' , type = str , default = 'US' , help = '-c <US>')

arguments = parseme.parse_args()

### api.openweathermap.org/data/2.5/weather?q={city name},{state},{country code}&appid={your api key} - By c
### api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key} - by ZipCode

weatherURL2 = 'http://api.openweathermap.org/data/2.5/weather?zip={0},{1}&appid={2}'.format(arguments.zipcode , arguments.country , os.getenv('OWM_API_KEY'))
try:
    req1 = requests.get(weatherURL2 ,  timeout=10)
except Exception as err:
    print(err)
else:
    if req1.status_code != 200:
        print("Unable to retrive link, please check the passed data and API_KEY")
    else:
        J_weather = req1.json()

try:
    def convertMe():
        temp = int(J_weather['main'].get('temp'))
        feels_like = int(J_weather['main'].get('feels_like'))
        pName = J_weather.get('name')
        sunrise = strftime('%Y-%B-%d %H:%M:%S', localtime(J_weather['sys'].get('sunrise')))
        sunset = strftime('%Y-%B-%d %H:%M:%S', localtime(J_weather['sys'].get('sunset')))
        temp = round(temp - 273.15 , 2)
        feels_like = round(feels_like - 273.15 , 2)
        return "Temperature in {2} : {0}\nBut it feels Like: {1}\nSunrise: {3}\nSunset: {4}".format(temp, feels_like, pName , sunrise , sunset)
except Exception as err:
    print(err)
else:
    try:
        print(convertMe())
    except NameError as err:
        print(err)