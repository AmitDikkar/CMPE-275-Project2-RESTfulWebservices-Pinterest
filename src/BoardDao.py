__author__ = 'Vijaya'

from dal import DBFactory
from couchquery import Database
import json

class BoardDao:

    @staticmethod
    def createboard(json):
        try:
            DBFactory.getdb().createDoc(json)
        except:
            raise

    @staticmethod
    def updateBoard(id, boardName, newBoard):
        try:
            doc = BoardDao.getUserDoc(id)
            boards = doc.boards
            for board in boards:
                    if board['boardName'].lower() == boardName:
                        board['boardName'] = newBoard['boardName']
                        board['boardDesc'] = newBoard['boardDesc']
                        board['category'] = newBoard['category']
                        board['isPrivate'] = newBoard['isPrivate']
                        DBFactory.getdb().updateDoc(doc)
                        return
        except:
            raise

    @staticmethod
    def getUserDoc(id):
        try:
            json = DBFactory.getdb().getDoc(id)
        except:
            raise
        return json

    @staticmethod
    def deleteBoard(id, boardName):
        try:
            doc = BoardDao.getUserDoc(id)
            boards = doc.boards
            for index in xrange(len(boards)):
                if boards[index]['boardName'] == boardName:
                    boards.pop(index)
                    DBFactory.getdb().updateDoc(doc)
                    return
        except:
            raise

    @staticmethod
    def getUserboards(id):
        try:
            msg = BoardDao.getUserDoc(id)
            return msg.boards
        except:
            raise

    @staticmethod
    def getBoardDetails(id, boardName):
        try:
            boardName = boardName.replace('-', ' ')
            boards = BoardDao.getUserboards(id)
            for board in boards:
                if board['boardName'].lower() == boardName:
                    return board
        except:
            raise