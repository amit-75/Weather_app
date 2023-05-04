from flask import Flask, jsonify,render_template,request
import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

app = Flask(__name__)

def scrap_info(city_name):
    url = 'https://www.timeanddate.com/weather/india/' + city_name
    ht = requests.get(url).content
    soup = BeautifulSoup(ht, 'html.parser')

    aa = soup.find('div', class_='bk-focus__qlook')
    if (aa != None):
        temp = aa.find('div', class_='h2').text
        nature = aa.find_all('p')[0].text

        div_1 = aa.find_all('p')[1].text.split('°C')
        feel_like = div_1[0].split(': ')[1]
        forcast = div_1[1].split(': ')[1]
        wind = div_1[2].split(': ')[1]

        div_2 = soup.find('div',class_='bk-focus__info')
        tr = div_2.find_all('tr')
        current_time = tr[1].find('td').text
        visibility = tr[3].find('td').text
        pressure = tr[4].find('td').text
        humidity = tr[5].find('td').text
        dew_point = tr[6].find('td').text
        return (city_name,temp,nature,feel_like,forcast,wind,current_time,visibility,pressure,humidity,dew_point)
    return None

@app.route('/', methods=['GET','POST'])
def weather():
    if request.method=="POST":
        try:
            city = request.form.get('city')
            (city,temp,nature,feel_like,forcast,wind,current_time,visibility,pressure,humidity,dew_point) = scrap_info(city)
            weather_info = [city,temp, nature, feel_like, forcast, wind, current_time, visibility, pressure, humidity, dew_point]
            return render_template('weather.html',weather_info=weather_info)
        except Exception as e:
            return '''
                <center>
                    <h3> Error Occur,<br></h3>
                    <a href="/">Back to page</a>
                </center>
                    '''

    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    (city,temp,nature,feel_like,forcast,wind,current_time,visibility,pressure,humidity,dew_point) = scrap_info(city)
    weather_info = [city,temp, nature, feel_like, forcast, wind, current_time, visibility, pressure, humidity, dew_point]
    return render_template('weather.html',weather_info=weather_info)
    # return weather_info




# @app.route('/', methods=['GET','POST'])
# def weather():
    
#     if request.method=="get":
#         city = request.form.get("city_name")
        
#         city_in = {
#          "city_name" : city
#         }

#         data=request.get_json(city_in)
#         print(data)
        # city=data["city"]
        # url = 'https://www.google.com/search?q=weather+"'+city+'"'
        # ht = requests.get(url).content
        # soup = BeautifulSoup(ht, 'html.parser')
        # aa = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
        # bb = aa[0].text
        # return "Temparatue : "+bb
    # if request.method=="GET":
    #     return jsonify(data)
    # return render_template('01_weather.html')

if __name__ == "__main__":
    app.run(debug='True', host='0.0.0.0', port='5000')