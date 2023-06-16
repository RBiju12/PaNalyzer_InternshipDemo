from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__, template_folder='Templates')

@app.route("/")
def index():
    return render_template("base.html")
@app.route("/home")
def home():
    try:
        url = "https://spanalytics.com/product/panalyzr/"

        page = requests.get(url)
        print("Page status code:", page.status_code)  

        soup = BeautifulSoup(page.text, 'html.parser')

        supports = soup.find_all('p')[5].text
        sales = soup.find_all('p')[6].text
        agreement = soup.find_all('p')[7].text

        texts_lis = [supports, sales, agreement]

        if len(texts_lis) == 0:
            raise ReferenceError
        else:
            return render_template('home.html', texts=texts_lis)

    except requests.exceptions.RequestException as e:
        print("Exception:", str(e))  
        return "Website does not permit scraping or is JavaScript driven"

@app.route("/overview")
def overview():
    try:
        url = "https://spanalytics.com/product/panalyzr/"

        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')


        overview = soup.find_all('p')[4]

        features = soup.find_all('li')[41:53]

        feauture_lis = []

        for i in features:
            feature = i.text
            feauture_lis.append(feature)

        if len(feauture_lis) == 0:
            return "Empty List"
        
        else:
            return render_template('overview.html', overview=overview, feauture_lis=feauture_lis)

    except requests.exceptions.RequestException as e:
        print("Exception:", str(e))  
        return "Website does not permit scraping or is JavaScript driven"
    


@app.route('/service')
def service():
    return render_template("service.html")


@app.route('/<user>')
def welcome(user):
    return f'Hello {user}!, Welcome to the PaNalyzer'



if __name__ == '__main__':
    app.run(debug=True)