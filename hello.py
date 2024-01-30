from db import db as Mongo
import constants as constant
from flask import Flask, make_response

app = Flask(__name__)
host = "127.0.0.1"
port = 3002

@app.route("/", methods=['GET', 'POST'])
def index():
   collection = Mongo[constant.EMPLOYEE]
   data = collection.find_one({}, {'_id': 0})
   response = make_response(data)
   response.headers['Content-Type'] = 'application/json'
   return response

if __name__ == '__main__':
   app.run(debug=True,host=host, port=port)