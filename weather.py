from flask import Flask, jsonify,render_template,request

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def weather():
    temp = None
    day_time = None
    if request.method=="POST":
        city = request.form.get('city_name')
    
        url = 'https://www.google.com/search?q=weather+"'+city+'"'
        ht = requests.get(url).content
        soup = BeautifulSoup(ht, 'html.parser')

        aa = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
        temp = aa[0].text

        bb = soup.find_all('div', class_='BNeawe tAd8D AP7Wnd')
        day_time = bb[0].text

        return render_template('weather.html',temp=temp,city=city,day_time=day_time)

    return render_template('weather.html',temp=temp,day_time=day_time)




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