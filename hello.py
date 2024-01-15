from flask import Flask

app = Flask(__name__)
host = "127.0.0.1"
port = 3002

@app.route("/")
def index():
   return "hello world!"

if __name__ == '__main__':
   app.run(debug=True,host=host, port=port)