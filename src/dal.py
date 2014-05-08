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


class CouchDB:

    url = "http://localhost:5984/pinterest"

    def __init__(self):
        self.db = Database(self.url)

    def getDoc(self, id):
        return self.db.get(id)

    def createDoc(self, json):
        return self.db.create(json)

    def deleteDoc(self, id):
        doc = self.getDoc(id)
        self.db.delete(doc)
