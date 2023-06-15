from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__, template_folder='Templates')

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/overview")
def overview():
    return render_template("overview.html")


@app.route('/service')
def service():
    return render_template("service.html")


@app.route('/<user>')
def welcome(user):
    return f'Hello {user}!, Welcome to the PaNalyzer'

@app.route('/hometext')
def scrape():
    try:
        url = "https://spanalytics.com/product/panalyzr/"

        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'lxml')

        supports  = soup.find_all('p')[5].text

        sales = soup.find_all('p')[6].text

        agreement = soup.find_all('p')[7].text

        texts_lis = [supports, sales, agreement]

        if len(texts_lis) == 0:
            raise ReferenceError
        else:
            return texts_lis, render_template('home.html')
    except:
        return "Website does permit Scraping or is JavaScript driven"
    

@app.route("/overviewtext")
def overviewtext():
    url = "https://spanalytics.com/product/panalyzr/"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')


    overview = soup.find_all('p')[4]

    features = soup.find_all('li')[41:53]

    feauture_lis = []

    for i in features:
        feature = i.text
        feauture_lis.append(feature)

    if len(feauture_lis) == 0:
        return "Empty List"
    else:
        return overview, feauture_lis, render_template('overview.html')


if __name__ == '__main__':
    app.run(debug=True)