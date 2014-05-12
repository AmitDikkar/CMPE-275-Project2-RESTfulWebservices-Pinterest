__author__ = 'Amit'

from bottle import request, response, route, run, template
from dal import CouchDB
import functools
import inspect
import string
from dal import DBFactory

class UserDao:
    db = DBFactory.getdb()

    def getDoc(self,id):
        return self.db.getDoc(id)


#move below function to UserDAO
    def updateUserProfile(self, id, json):
        print "Inside UserDao"
        doc = self.db.getDoc(id)
        doc["firstName"] = json["firstName"]
        doc["lastName"] = json["lastName"]
        doc["password"] = json["password"]
        self.db.updateDoc(doc)

#New Function is added to the DAL: can be used to check whether document already exists.
    def isExist(self,id):
        print "Inside isExist"
        print "Checking for: "+id
        try:
            doc = self.db.getDoc(id)
            print "UserDao-isExist: doc found in try"
            if doc is None:
                return False
            else:
                return True
        except Exception as e:
            print "UserDao-isExist: Exception"+e.message
            print "returning false now"
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
            doc = self.db.getDoc(userId)
            boards = doc["boards"]
            for board in boards:
                if board["boardName"] == boardName:
                    for pin in board["pins"]:
                        if pin["pinName"] == pinName:
                            if likeBy not in pin["likes"]:
                                pin["likes"].append(likeBy)
                                print "Appended here"
                                self.db.updateDoc(doc)
                                print "Updated in if"
                                return pin
                            else:
                                pin["likes"].remove(likeBy)
                                print "Removed from list: Unlike"
                                self.db.updateDoc(doc)
                                print "Updated in else"
                        print "Updated All"
                        return pin
            return None
        except Exception as e:
            print "Exception: inside LinkAngGetPin"
            print e.message
            return None

    def followAndUnfollowUser(self, followerId, followTo):
        print "UserDao: inside followAndUnfollowUser"
        try:
            followerDoc = self.db.getDoc(followerId)
            followToDoc = self.db.getDoc(followTo)
            print "UserDao: Both docs exists"

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

            self.db.updateDoc(followerDoc)
            self.db.updateDoc(followToDoc)
            print "Updated both docs"
            #return only the resource of follower
            newdoc = self.db.getDoc(followerId)
            print newdoc
            return newdoc
        except Exception as e:
            print "Exception: UserDao followAndUnfollow user"
            print e.message
            return None

