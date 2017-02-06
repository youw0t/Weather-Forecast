import requests
import json
import os
import datetime

clear = lambda: os.system('cls')

# http://openweathermap.org/api  API Key is needed, you can register a free account
api_key = '6f6e7455de97fc8bb0109e01f8dbdbdc'

def checkLang():
    while True:
        lang = input("Enter language (example: NL): \n")
        if len(lang) > 2:
            print("Type 2 letters")
            continue
        else:
            break
    return lang
    # if len(lang) > 2:
    #     print("Type NL or EN, retard")

language = checkLang()

def weather(cit):
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + cit + '&mode=json&units=metric&cnt=5' + '&lang=' + language + '&units=metric&appid=' + api_key
    obj = requests.get(url).text
    data = json.loads(obj)
    count = data['city']['country']
    print(data['city']['name'] + ", " + count)
    print("---------------------------")
    for item in data['list']:
        print(datetime.datetime.fromtimestamp(int(item['dt'])).strftime("%A %d/%m/%Y, %H:%M"))
        default = item['weather'][0]['main']  # Clouds
        desc = item['weather'][0]['description']  # cloudy weather
        temp = (item['temp']['day'] + item['temp']['min'] + item['temp']['max'] + item['temp']['night'] + item['temp']['eve'] + item['temp']['morn']) / 6
        print(default + ", " + desc + "\n" + "Average temp: " + ("{0:.2f}".format(temp)) + "ºC\n---------------------------")

while True:
    choice = input("Enter city, enter clear to clear screen or type quit to leave: \n").lower()
    if choice == 'quit':
        break
    elif choice == 'clear':
        clear()
    else:
        weather(choice)
