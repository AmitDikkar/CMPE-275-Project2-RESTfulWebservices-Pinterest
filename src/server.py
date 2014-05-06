from bottle import request, response, route, run, template
from dal import CouchDB

dao = CouchDB()

#Sign Up constants
signup_error = 'Error occured during sign up. Please try later'
signup_response = '{ "links" : [{"url":"/users/login/","method": "POST"}]}'

@route('/signup') # or @post('/services/signup')
def get():
    return "Hello Bottle"

@route('/signup', method='POST') # or @post('/services/signup')
def signup():
    json = request.json
    msg = signup_error
    try:
        dao.createDoc(json)
        msg = signup_response
    except:
        response.statusCode = 400
    return msg

@route('/login', method='POST')
def login():
    json = request.json
    return "Authenticating " + json['email']

@route('/user/<id>', method='DELETE')
def deleteUser(id):
    return template("Deleting user {{userId}}.", userId=id)

run(host='localhost', port=8080)