"""
***************************************************
Title: ISS API
Author: Brogan Avery
Created: 2020-010-16
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

import requests
import json
from datetime import datetime
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
#current location
    response = requests.get("http://api.open-notify.org/iss-now.json")

    pythoned_json = json.loads(response.text)

    long = pythoned_json['iss_position']['longitude']
    lat = pythoned_json['iss_position']['latitude']

    print('the space station is at: \n  longitude: ', long, '\n  latitude: ', lat)

#people
    response = requests.get("http://api.open-notify.org/astros.json")

    pythoned_json = json.loads(response.text)

    numOfPeople = 0
    for i in pythoned_json['people']:
        numOfPeople = numOfPeople + 1

    print('\nPeople on space station:')
    for i in range(numOfPeople):
        print(' ',pythoned_json['people'][i]['name'])

# next times over ankeny
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat=41.7318&lon=93.6001")

    pythoned_json = json.loads(response.text)

    print('\n','timestamps:')
    for i in range(5):
        print('  ',pythoned_json['response'][i]['risetime'])
