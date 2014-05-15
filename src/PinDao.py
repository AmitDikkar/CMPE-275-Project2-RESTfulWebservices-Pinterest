#-------------------------------------------------------------------------------
# Name:        PinDao
# Purpose:
#
# Author:      anup
#
# Created:     11/05/2014
# Updated By:  Hrishikesh P
# Update Date: 12/05/2014
# Update Desc: Added functions to add,delete comments
#   
# Copyright:   (c) anup 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from dal import DBFactory
from couchquery import Database
import json
from constants import Constants

class PinDao:

    @staticmethod
    def addNewPin(userId, boardName,json):
            try:
                 #doc = self.db.get(userId)
                 doc = PinDao.getUserDoc(userId)
                 boards = doc["boards"]
                 count = 0
                 for board in boards:
                    if board["boardName"] == boardName:
                        if not Constants.PINS in board:
                            doc.boards[count][Constants.PINS] = []

                        doc.boards[count][Constants.PINS].append(json)
                        DBFactory.getdb().updateDoc(doc)
                        return "New Pin added"

                    count += 1
                 return None

            except Exception as e:
                print e.message

    @staticmethod
    def getPin(UserId,boardName,pinName):
            try:
                #doc = self.db.get(UserId)
                doc = PinDao.getUserDoc(UserId)
                boards = doc["boards"]
                for board in boards:
                    if board["boardName"] == boardName:
                        for pin in board["pins"]:
                            if pin["pinName"] == pinName:
                                return pin
                return None
            except Exception as e:
                print e.message
                print 'error in getting pin'

    @staticmethod
    def getAllPins(UserId,boardName):
            try:
                #doc = self.db.get(UserId)
                doc = PinDao.getUserDoc(UserId)
                boards = doc["boards"]
                for board in boards:
                    if board["boardName"] == boardName:
                        return board
            except Exception as e:
                print e.message
                print 'error in getting board'

    @staticmethod
    def deletePin(UserId,boardName,pinName):
            i = 0
            try:
                #doc = self.db.get(UserId)
                doc = PinDao.getUserDoc(UserId)
                boards = doc["boards"]
                for board in boards:
                    if board["boardName"] == boardName:
                        pins = board["pins"]
                        print len(pins)
                        for index in xrange(len(pins)):
                            print(pins[index]['pinName'])
                            if pins[index]['pinName'] == pinName:
                                pins.pop(index)
                                #self.db.save(doc)
                                DBFactory.getdb().updateDoc(doc)
                                return "pin deleted"
                return None
            except Exception as e:
                print e.message
                print 'error in deleting pin'
                return None

    @staticmethod
    def updatePin(UserId,boardName,json,pinName):
            try:
                #doc = self.db.get(UserId)
                doc = PinDao.getUserDoc(UserId)
                boards = doc["boards"]
                for board in boards:
                    if board["boardName"] == boardName:
                        for pin in board["pins"]:
                            print pin
                            if pin["pinName"] == pinName:
                                pin['pinName'] = json['pinName']
                                pin['image'] = json['image']
                                pin['description'] = json['description']
                                #self.db.save(doc)
                                DBFactory.getdb().updateDoc(doc)
                                return "pin updated"
                return None
            except Exception as e:
                print e.message
                print 'error in updating pin'
                return None

    @staticmethod
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

    @staticmethod
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

    #Comments related functions
    @staticmethod
    def addNewComment(self,userId, boardName, pinName,json):
        try:
             doc = DBFactory.getdb().getDoc(userId)
             boards = doc[Constants.BOARDS]
             board_index = pin_index = 0

             for board in boards:
                if board[Constants.BOARDNAME] == boardName:
                    pins = board[Constants.PINS]
                    for pin in pins:
                        if pin['pinName'] == pinName:
                            if not 'comments' in pin:
                                doc.boards[board_index].pins[pin_index]['comments'] = []

                            doc.boards[board_index].pins[pin_index]['comments'].append(json)

                            DBFactory.getdb().updateDoc(doc)
                            print "New comment added for the pin : " + pinName
                            return
                    pin_index += 1
                board_index += 1

        except Exception as e:
            print e.message
            print 'error in adding new comment'

    @staticmethod
    def getComment(self,UserId,boardName,pinName,addedBy,comment):
        try:
            doc = self.db.get(UserId)
            boards = doc["boards"]
            for board in boards:
                if board["boardName"] == boardName:
                    for pin in board["pins"]:
                        if pin["pinName"] == pinName:
                         comments = pin['comments']
                         for index in xrange(len(comments)):
                            if comments[index]['addedby']==addedBy:
                                if comments[index]['comment']==comment:
                                  return comments[index]['comment']
            return None
        except Exception as e:
            print e.message
            print 'error in fetching comment'

    @staticmethod
    def getAllComments(self,UserId,boardName,pinName):
        try:
            doc = self.db.get(UserId)
            boards = doc["boards"]
            for board in boards:
                try:
                 if board["boardName"] == boardName:
                    pins = board["pins"]
                    for pin in pins:
                      if pin['pinName'] == pinName:
                       comments = pin['comments']
                       return comments
                except Exception as err:
                    print err.message
        except Exception as  e:
            print e.message
            print 'error fetching all comments'

    @staticmethod # Comment deletion 
    def deleteComment(self,UserId,boardName,pinName,addedBy,comment):
        i = 0
        print 'Delete comment called'
        try:
            doc = self.db.get(UserId)
            boards = doc["boards"]
            for board in boards:
                if board["boardName"] == boardName:
                    pins = board["pins"]
                    for pin in pins:
                      try:
                          if pin['pinName'] == pinName:
                           print 'Inside delete comment loop'
                           comments = pin['comments']

                           for index in xrange(len(comments)):#Find comment using comment details
                               if comments[index]['addedby']==addedBy:
                                if comments[index]['comment']==comment:

                                    print 'deleting comment'+comment+ '#'+'Added By:'+addedBy
                                    
                                    comments.pop(index)
                                    self.db.save(doc)
                                    print 'Comment successfully deleted...'
                                    return 'Success'

                      except Exception as err:
                          print err.message

            return None
        except Exception as e:
            print e.message
            print 'error in deleting comment'


 
    @staticmethod
    def getUserDoc(id):
        try:
            json = DBFactory.getdb().getDoc(id)
        except:
            raise
        return json