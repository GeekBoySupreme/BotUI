from flask import Flask, request
from flask_cors import CORS
from code import getresponse, getresponse2

app = Flask(__name__)
CORS(app)

response = getresponse()
response1 = getresponse2()

@app.route('/hello')
def get_response():
  return response

@app.route('/hi')
def get_response1():
  return response1

if __name__ == "__main__":
    app.run()