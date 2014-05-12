from bottle import request, response, route, run, error, delete, put, get, post
from constants import Constants
from src.user import User
from util import Util
from BoardDao import BoardDao
import json

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


@post('/users/<id>/boards')
def createboard(id):
    json = request.json
    msg = Constants.create_board_error
    try:
        BoardDao.createboard(json)
        msg = form_createboard_response(id, json[Constants.BOARD_NAME])
        response.status = Constants.RESOURCE_CREATED #Successful creation of a resource
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR
        return e


@put('/users/<id>/boards/<boardName>')
def updateboard(id, boardName):
    json = request.json
    msg = Constants.update_board_error
    boardName = boardName.replace(Constants.HYPHEN, Constants.WHITESPACE)
    try:
        BoardDao.updateBoard(id, boardName, json)
        msg = form_getboard_response(id, json)
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR
        return e

@get('/users/<id>/boards')
def getAllUserboards(id):
    msg = Constants.get_boards_error
    try:
        msg = BoardDao.getUserboards(id)
        msg = json.dumps(msg)
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR
        return e
    return msg


@delete('/users/<id>/boards/<boardName>')
def deleteBoard(id, boardName):
    boardName = boardName.replace(Constants.HYPHEN, Constants.WHITESPACE)
    msg = Constants.delete_board_error
    try:
        BoardDao.deleteBoard(id, boardName)
        msg = Constants.delete_board_response.replace(Constants.USERID, id)
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR
        return e

@get('/users/<id>/boards/<boardName>')
def getBoardDetails(id, boardName):
    msg = Constants.get_board_error
    try:
        json = BoardDao.getBoardDetails(id, boardName)
        msg = form_getboard_response(id, json)
        return msg
    except Exception as e:
        response.status = Constants.INTERNAL_SERVER_ERROR
        return e

def form_getboard_response(id, board):
    response_message = Constants.get_board_response.replace(Constants.BOARD_NAME_VALUE, board[Constants.BOARD_NAME])
    response_message = response_message.replace(Constants.BOARD_DESC_VALUE, board[Constants.BOARD_DESC])
    response_message = response_message.replace(Constants.CATEGORY_VALUE, board[Constants.CATEGORY])
    isPrivate = str(board[Constants.ISPRIVATE])
    response_message = response_message.replace(Constants.IS_PRIVATE_VALUE, isPrivate)
    #remove extra white spaces from board name
    response_message = response_message.replace(Constants.USERID, id)
    response_message = response_message.replace(Constants.BOARD_NAME, board[Constants.BOARDNAME])
    return response_message


def form_createboard_response(id, boardname):
    response_msg = Constants.create_board_response
    response_msg = response_msg.replace(Constants.USERID, id)
    boardname = Constants.WHITESPACE.join(boardname.split())
    boardname = boardname.replace(Constants.WHITESPACE, Constants.HYPHEN)
    response_msg = response_msg.replace(Constants.BOARD_NAME, boardname)
    return response_msg


run(host='localhost', port=8080)