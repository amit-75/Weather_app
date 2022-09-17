from flask import Flask,render_template,request
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


if __name__ == "__main__":
    app.run(debug='True', host='0.0.0.0', port='5000')
