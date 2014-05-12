#-------------------------------------------------------------------------------
# Name:        PinDao
# Purpose:
#
# Author:      anup
#
# Created:     11/05/2014
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


    @staticmethod
    def getUserDoc(id):
        try:
            json = DBFactory.getdb().getDoc(id)
        except:
            raise
        return json