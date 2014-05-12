from dal import DBFactory
from constants import Constants
from util import Util
from UserDao import UserDao
from bottle import response
dao = UserDao()

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

    def updateUserProfile(self, userId, json):
        print "inside updateUserProfile"
        if dao.isExist(userId):
            try:
                dao.updateUserProfile(userId, json)
                #if successful return 200 code and the updated doc
                newDoc = dao.getDoc(userId)
                newDoc.__delitem__("_rev")
                newDoc.__delitem__("_id")
                #return newDoc
                print "User: new doc created"
                return [None,response,newDoc]
            except Exception as e:
                #if any exception, set status as 500
                response.status = 500
                print e.message
                # and return error message
                return [e.message,response,None]
        else:
            #if doc doesn't exists, set status = 400 (Bad request)
            response.status = 400
            #send error message in response
            #return "Record with the given id doesn't exist"
            return ["Record with the given id doesn't exist",response,None]

    def likePin(self,userId, pinOf, boardName, pinName):
        print "user: inside Like"
        if dao.isExist(userId) & dao.isExist(pinOf):
            print "both users exists"
            if dao.isPinExist(pinOf, boardName, pinName):
                print "Yes..pin exists"
                pin = dao.likeAndGetPin(userId, pinOf, boardName, pinName)
                if pin is None:
                    #return "Error in Updating followers"
                    #response.status = 400
                    return ["Error in Updating followers", 400, None]
                else:
                    #response.status = 201
                    #return pin
                    return [None,201,pin]
            else:
                print "Either there are no pins or pin doesn't exists"
                #response.status = 400
                #return "both users exists and but pin Doesn't exist"
                return ["both users exists and but pin Doesn't exist",400,None]
        else:
            print "either or both user names are incorrect"
            #Userids sent are incorrect. Set status=400 (Bad Request)
            #response.status = 400
            #return "either or both user names are incorrect"
            return ["either or both user names are incorrect", 400, None]

    def followUser(self, userId, followTo):
        try:
            if dao.isExist(userId) & dao.isExist(followTo):
                print "Both users exists..proceed"
                doc = dao.followAndUnfollowUser(userId,followTo)
                if doc is None:
                    #return "Error in updating followers"
                    print "User: followUser - None detected"
                    return ["Error in updating followers", 400, None]
                else:
                    #response.status = 201
                    #return doc
                    print "Not None"
                    print doc
                    return [None, 201, doc]
            else:
                print "Either one of the users doesn't exists"
                #response.status = 400
                #return "Either one of the user Ids provided doesn't exists"
                return ["Either one of the user Ids provided doesn't exists", 400, None]
        except Exception as e:
            return [e.message, 400, None]
