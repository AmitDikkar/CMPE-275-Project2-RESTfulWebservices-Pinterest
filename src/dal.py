#-------------------------------------------------------------------------------
# Name:        dal
# Purpose:
#
# Author:      Joel
#
# Created:     05/05/2014
# Copyright:   (c) Joel 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from couchquery import Database
from collections import OrderedDict
from threading import Lock
from constants import Constants


class CouchDB:

    lock = Lock()

    def __init__(self):
        self.write_db = Database(Constants.WRITE_URL)
        self.read_db = Database(Constants.READ_URL)
        self.cache = OrderedDict()

    def getDoc(self, id):
        document = None

        self.lock.acquire()

        if id not in self.cache.keys():  #document not in cache
            document = self.read_db.get(id)

            if self.cache.__len__() == Constants.CACHE_SIZE:
                self.cache.popitem(False)  #remove the oldest entry from cache

            self.cache.__setitem__(id,  document)
        else:  #get from cache
            document = self.cache.__getitem__(id)

        self.lock.release()

        return document

    def createDoc(self, json):
        return self.write_db.create(json)

    def deleteDoc(self, id):
        self.lock.acquire()
        doc = self.getDoc(id)
        self.cache.pop(id)  #clear document from cache
        self.write_db.delete(doc)
        self.lock.release()

    def saveDoc(self, doc):
        self.db.save(doc)

    def updateDoc(self, doc):
        self.lock.acquire()
        self.cache.pop(doc[Constants.DOCUMENT_ID])  #clear document from cache
        self.write_db.update(doc)
        self.lock.release()


class DBFactory:

    db = None
    @staticmethod
    def getdb():
        if DBFactory.db is None:
            db = CouchDB()
        return db
