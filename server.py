from flask import Flask, request
from flask_cors import CORS
from code import getresponse, getresponse2

app = Flask(__name__)
CORS(app)


#extra routes resulting 404 errors for reasons unknown
#an array created here shall take in and store the user variables
@app.route('/hi')
def get_response1():
  return getresponse2()

@app.route('/hello')
def get_response():
  return getresponse()

@app.route('/exit')
def get_response2():
  return getresponse3()


if __name__ == "__main__":
    app.run()