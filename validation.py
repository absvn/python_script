import json
import time
from flask import Flask, request, jsonify
from flask_allowedhosts import limit_hosts
from flask_cors import CORS
from domain_validation.whois import WHOIS
import requests
from email_validator import validate_email, EmailNotValidError
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

class validation:
    def ping_url(self, url):
        try:
            response = requests.head(url, timeout=5)  
            if response.status_code == 200 or response.status_code == 301:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False
        except requests.Timeout:
            return False

    def domain_verify(self, domain):
        temp = WHOIS(domain)
        if temp.creation_date() == 'Creation_date_not_found' or temp.registrar() == 'Registrar_not_found':
            return False
        else:
            return True

@app.route('/validation',methods=["POST"])
def score():
    start = time.time()

    dict_score = {"success" : "False",
                  "validation" : "Failed",
                  "score" : "-"
                  }
    try:
        string_email = request.data
        atomic_dict = json.loads(string_email)
        email = atomic_dict.get('email')
        domain = email.split('@')[1]
        url = 'https://www.'+ domain
        response = requests.head(url)
        print(response.status_code)
        valobj = validation()
        ping_status = valobj.ping_url(url)
        print(ping_status)
        domain_status = valobj.domain_verify(domain)
        print(domain_status)
        if ping_status == True and domain_status == True:
            dict_score["validation"] = 'Success'
            dict_score["score"] = str(round(random.uniform(90,100),2))
            dict_score["success"] = 'True'
        else:
            dict_score["score"] = str(round(random.uniform(10,20),2))
            dict_score["success"] = 'True'
        return dict_score
        
    except Exception as e:
        print(str(e))
    end = time.time()
    dict_score['time taken'] = end-start
    return jsonify(dict_score)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port="8888")

