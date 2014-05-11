from bottle import request, response, route, run, error
from constants import Constants
from src.user import User

'''error routes'''


@error(404)
def error404(error):
    return 'Sorry. Nothing here. Try /users/login or /signup'


'''user resource routes '''

def validateinput(request):
    try:
        return request.json
    except:
        return None

@route('/signup', method='POST')  # or @post('/services/signup')
def signup():
    json = validateinput(request)
    if json is None:
        return Constants.ERROR_INVALID_INPUT

    try:
        user = User()
        msg = user.registeruser(json)
        response.status = Constants.RESOURCE_CREATED  #resource created successfully
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR  #internal server error
        return e

@route('/users/login', method='POST')
def login():
    json = validateinput(request)
    if json is None:
        return Constants.ERROR_INVALID_INPUT

    try:
        user = User()
        msg = user.authenticateuser(json)
        response.status = Constants.ACCEPTED  #login request successful
        return msg
    except Exception as e:
        response.status = Constants.AUTH_ERROR  #authentication failed
        return e

'''board resource routes'''

run(host='localhost', port=8080)