from flask.json import jsonify
import os, json
from flask import Flask, request
from werkzeug.utils import import_string
from itsdangerous import JSONWebSignatureSerializer
from flask_sqlalchemy import SQLAlchemy

# APP_INIT
app = Flask(__name__)
cfg = import_string(os.environ['EXAMPLE_MODE'])()
app.config.from_object(cfg)
s = JSONWebSignatureSerializer(app.config['SECRET_KEY'])


sqldb = SQLAlchemy(app)

# Set up your model here
from model.ExampleTable import Example_Table
sqldb.create_all()
sqldb.session.commit()

# Import your handlers here 
from handler.example_handler import *

''' 
    GET Example:
    Print out basic app information, if you start up app in "dev" mode;
    otherwise, print out "Hello World" in "prod" mode.
'''
@app.route('/GET/dev_or_prod', methods=['GET'])
def index():
    if app.config["DEBUG"]:
        # DEV ENV
        configInfo = ""
        for key, val in app.config.items():
            configInfo += "{} : {} <br>".format(key,val)
        return configInfo
    else:
        # PROD ENV
        return "Hello world!"


''' 
    POST Example:
    Receive data from frontend. You could choose any format you like. 
    For instance, we use "json" as the format of request data here.
    For more information, please check the documents: https://flask.palletsprojects.com/en/2.0.x/api/#incoming-request-data
'''
@app.route('/POST/storedata', methods=['POST'])
def StoreData():
    '''
        Copy data down below and fill into "raw" columns in the Postman or some other API test services
    
        *** Example JSON Data ***
        [{ 'name':'Yuwei Liu',
           'timestamp':'2022/03/12-10:00:00',
           'lucky_number':17 }]
    
    '''
    data = request.json
    error, result = example_ReceivedAndStored(data)
    return _process_result(error, result)


def _process_result(error, result):
	return jsonify({"error":error, "result":result})