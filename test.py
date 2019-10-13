from flask import Flask
from flask_cors import CORS
from code import getresponse, getresponse2
app = Flask(__name__)
CORS(app)

@app.route('/hello/<name>')
def route_response(name):
   return getresponse2()

@app.route('/hi/<name>')
def route_response1(name):
   return getresponse()


if __name__ == '__main__':
   app.run()