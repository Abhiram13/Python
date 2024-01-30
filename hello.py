from db import db as employeeCollection
import constants as constant
from flask import Flask, make_response, request
from controllers.login import LoginController
from collections import namedtuple
import json

app = Flask(__name__)
host = "127.0.0.1"
port = 3002

@app.route("/", methods=['GET', 'POST'])
def index():
   collection = employeeCollection
   data = collection.find_one({}, {'_id': 0})
   response = make_response(data)
   response.headers['Content-Type'] = 'application/json'
   return response

def CustomHook(obj):
   return namedtuple('X', obj.keys())(*obj.values())

@app.route("/login", methods=['POST'])
def login():
   payload = request.data
   data = json.loads(payload, object_hook=CustomHook)
   return LoginController.fetchEmployee(data.email, data.password)

if __name__ == '__main__':
   app.run(debug=True,host=host, port=port)