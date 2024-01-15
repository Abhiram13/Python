from flask import Flask, request, make_response

app = Flask(__name__)
host = "127.0.0.1"
port = 3002

@app.route("/", methods=['GET', 'POST'])
def index():
   print(request.data)
   response = make_response("Hello Client!");
   response.headers['Content-Type'] = 'application/json'
   return response;

if __name__ == '__main__':
   app.run(debug=True,host=host, port=port)