from dal import DBFactory
from constants import Constants
from util import Util


class User:

    def __init__(self):
        self.connection = DBFactory.getdb()

    def registeruser(self, user):

        if user is None:
            raise ValueError(Constants.ERROR_INVALID_INPUT)

        if Constants.EMAIL not in user:
            raise ValueError(Constants.ERROR_INVALID_EMAIL)

        if Constants.FIRST_NAME not in user:
            raise ValueError(Constants.ERROR_INVALID_FIRST_NAME)

        try:
            userid = Util.normalizestring(user[Constants.EMAIL])
            user[Constants.DOCUMENT_ID] = userid
            self.connection.createDoc(user)
            return Constants.RESPONSE_SIGNUP
        except:
            raise Exception(Constants.ERROR_DB)

    def authenticateuser(self, user):

        if user is None:
            raise ValueError(Constants.ERROR_INVALID_INPUT)

        if Constants.EMAIL not in user:
            raise ValueError(Constants.ERROR_INVALID_EMAIL)

        doc = []
        userid = Util.normalizestring(user[Constants.EMAIL])
        try:
            doc = self.connection.getDoc(userid)
        except:
            raise Exception(Constants.ERROR_DB)

        if user[Constants.PASSWORD] == doc[Constants.PASSWORD]:
            return Constants.RESPONSE_LOGIN.replace(Constants.USER_ID,doc[Constants.DOCUMENT_ID])
        else:
            raise Exception(Constants.ERROR_LOGIN)

