from flask import Flask
from flask.ext.api.exceptions import APIException

class ServiceUnavailable(APIException):
    status_code = 503
    detail = 'Service temporarily unavailable, try again later.'




app = Flask(__name__)
app.myHealth=100

@app.route('/')
def hello_world():
    return 'Hello World !'
    
@app.route('/health')
def getHealth():
    if app.myHealth!=100:
       raise ServiceUnavailable()
    else:
       return "Health Is Good"
        
@app.route('/ready')
def  areYouReady():
    return 'yes'
    
@app.route('/makeUnhealthy')
def  makeUnHealthy():
    app.myHealth=0
    return "I'm sick"
    
@app.route('/makeHealthy')
def  makeHealthy():
    app.myHealth=100
    return "I'm healthy"



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

