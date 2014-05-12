from bottle import request, response, route, run, error
from constants import Constants
from user import User
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

@route('/users/<userId>', method='PUT')
def updateUserProfile(userId):
    print "Inside server.py"
    json = request.json
    responceList = user.updateUserProfile(userId, json)
    if responceList[0] is not None:
        print "not null"
        response = responceList[1]
        doc = responceList[2]
        return doc
    else:
        response = responceList[1]
        return responceList[2]

@route('/users/<userId>/pins/likeResourse', method="POST")
def likepin(userId):
    """
        :param userId:
        :param boardName:
        :param pinId:
    """
    json = request.json
    try:
        pinOf = json["pinOf"]
        boardName = json["boardName"]
        pinName = json["pinName"]
        print "All retrieved"
        responceList = user.likePin(userId,pinOf,boardName,pinName)
        if responceList[0] is not None:
            print "not null"
            response.status = responceList[1]
            doc = responceList[2]
            return doc
        else:
            response.status = responceList[1]
            return responceList[2]
    except Exception as e:
        print "Server:inside except"
        print e.message
        #one of the required fields are missing. Set status=400 (Bad Request)
        response.status = 400
        return e.message

@route('/users/<userId>/follows',method="POST")
def followUser(userId):
    print "userId:"+userId
    print request.query['followTo']
    try:
        followTo = request.query['followTo']
        responseList = user.followUser(userId,followTo)
        if responseList[0] is not None:
            print "not null"
            response.status = responseList[1]
            return responseList[0]
        else:
            response.status = responseList[1]
            return responseList[2]
    except:
        print "Exception in FollowUser"
        response.status = 400
        return "Error: Please provide all required fields"

run(host='localhost', port=8080)