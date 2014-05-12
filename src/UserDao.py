__author__ = 'Amit'

from bottle import request, response, route, run, template
from dal import CouchDB
import functools
import inspect
import string
from dal import DBFactory

class UserDao:
    db = DBFactory.getdb()

#move below function to UserDAO
    def updateDoc(self, id, json):
        print "Inside UserDao"
        doc = self.db.getDoc(id)
        doc["firstName"] = json["firstName"]
        doc["lastName"] = json["lastName"]
        doc["password"] = json["password"]
        self.db.update(doc)

#New Function is added to the DAL: can be used to check whether document already exists.
    def isExist(self,id):
        print "Inside isExist"
        try:
            doc = self.db.getDoc(id)
            print "UserDao-isExist: doc found in try"
            return True
        except Exception as e:
            print "UserDao-isExist: Exception"+e.message
            return False

#move below function to PinDAO
    def isPinExist(self,id,boardName, pinName):
        try:
            doc = self.db.getDoc(id)
            boards = doc["boards"]
            for board in boards:
                if board["boardName"] == boardName:
                    for pin in board["pins"]:
                        if pin["pinName"] == pinName:
                            return True
            return False
        except Exception as e:
            print e.message
            return False

#Move below function to PinDao
    def likeAndGetPin(self,likeBy, userId, boardName, pinName):
        try:
            doc = self.db.get(userId)
            boards = doc["boards"]
            for board in boards:
                if board["boardName"] == boardName:
                    for pin in board["pins"]:
                        if pin["pinName"] == pinName:
                            if likeBy not in pin["likes"]:
                                pin["likes"].append(likeBy)
                                print "Appended here"
                                self.db.update(doc)
                                print "Updated in if"
                                return pin
                            else:
                                pin["likes"].remove(likeBy)
                                print "Removed from list: Unlike"
                                self.db.update(doc)
                                print "Updated in else"
                        print "Updated All"
                        return pin
            return None
        except Exception as e:
            print "Exception: inside LinkAngGetPin"
            print e.message
            return None

    def followAndUnfollowUser(self, followerId, followTo):
        try:
            followerDoc = self.db.get(followerId)
            followToDoc = self.db.get(followTo)

            #add followTo to follows list of FollowerId
            if followTo not in followerDoc["follows"]:
                followerDoc["follows"].append(followTo)
            else:
                followerDoc["follows"].remove(followTo)

            #add followersID to followers list of FollowTo
            if followerId not in followToDoc["followers"]:
                followToDoc["followers"].append(followerId)
            else:
                followToDoc["followers"].remove(followerId)

            self.db.update(followerDoc)
            self.db.update(followToDoc)
            print "Updated both docs"
            #return only the resource of follower
            return self.db.get(followerId)
        except Exception as e:
            print e.message
            return None

