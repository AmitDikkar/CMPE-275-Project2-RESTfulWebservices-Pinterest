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
from couchquery import *

class CouchDB:

    url = "http://localhost:5984/pinterest"

    def __init(self):
        self.db = Database(url)

    def getDoc(self,id):
        return self.db.get(id)

    def createDoc(self, json):
        return db.create(json)

    def deleteDoc(self, id):
        doc = getDoc(id)
        db.delete(doc)



