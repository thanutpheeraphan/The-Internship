import requests
import flask
from flask import request, jsonify
from bs4 import BeautifulSoup

## Question 4.1
start_url = requests.get('https://theinternship.io/')
soup = BeautifulSoup(start_url.text, 'html.parser')
image_tags = soup.findAll('img',class_ ='center-logos')
description_tags = soup.findAll('span',class_ ='list-company')
companies = {}
companies_api = []
final_companies_api = []
for i in range (len(image_tags)):
    companies[image_tags[i].get('src')] = len(description_tags[i].get_text())

companies = {key: value for key, value in sorted(companies.items(), key=lambda item: item[1])}

for image_source in companies.keys():
    print(image_source)

## Question 4.2
for image_source in companies.keys():
    final_image_source = 'https://theinternship.io/' + image_source
    companies_api.append({'logo' : final_image_source})

final_companies_api = {'companies' : companies_api}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/companies', methods=['GET'])

def gen_api():
    return jsonify(final_companies_api)

app.run()
