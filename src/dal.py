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

    def getdoc(self,id):
        return self.db.get(id)

    def createdoc(self, json):
        return self.db.create(json)

    def deletedoc(self, id):
        doc = self.getDoc(id)
        self.db.delete(doc)



