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
                 for board in boards:
                    if board["boardName"] == boardName:
                        board['pins'].append(json)
                        #self.db.save(doc)
                        DBFactory.getdb().saveDoc(doc)
                        return "New Pin added"
                 return

            except Exception as e:
                print e.message
                print 'error in adding new pin'

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
                                DBFactory.getdb().saveDoc(doc)
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
                                DBFactory.getdb().saveDoc(doc)
                                return "pin updated"
                return None
            except Exception as e:
                print e.message
                print 'error in updating pin'
                return None


    #Comments related functions
    @staticmethod
    def addNewComment(self,userId, boardName,pinName,json):
        noOfPins = 0
        try:
             doc = self.db.get(userId)
             boards = doc["boards"]
             noOfPins = len(boards)
             print json
             for board in boards:
                if board["boardName"] == boardName:
                    pins=board["pins"]
                    for pin in pins:
                      try:
                        print 'Inside add comment loop '
                        if pin['pinName'] == pinName:
                            print 'appending new comment'
                            pin['comments'].append(json)
                            self.db.update(doc)
                            print "New comment added for the pin:"+ pinName
                            return
                      except Exception as err:
                          print err.message
                   # board['pins'].append(json)
                   # self.db.save(doc)

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