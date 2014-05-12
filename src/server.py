from bottle import request, response, route, run, error
from constants import Constants
from src.user import User
from util import Util

'''error routes'''


@error(404)
def error404(error):
    return 'Sorry. Nothing here. Try /users/login or /signup'


'''user resource routes '''
user = User()


def validate_input(request):
    try:
        return request.json
    except:
        return None


def is_user_authenticated(request):
    if request.get_cookie(Constants.COOKIE_KEY):
        return True
    return False

@route('/signup', method='POST')  # or @post('/services/signup')
def signup():
    json = validate_input(request)
    if json is None:
        return Constants.ERROR_INVALID_INPUT

    try:
        msg = user.registeruser(json)
        response.status = Constants.RESOURCE_CREATED  #resource created successfully
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR  #internal server error
        return e

@route('/users/login', method='POST')
def login():
    json = validate_input(request)
    if json is None:
        return Constants.ERROR_INVALID_INPUT

    try:
        msg = user.authenticateuser(json)
        response.set_cookie(Constants.COOKIE_KEY, Util.normalizestring(json[Constants.EMAIL]))
        response.status = Constants.ACCEPTED  #login request successful
        return msg
    except Exception as e:
        response.status = Constants.AUTH_ERROR  #authentication failed
        return e

'''board resource routes'''

run(host='localhost', port=8080)