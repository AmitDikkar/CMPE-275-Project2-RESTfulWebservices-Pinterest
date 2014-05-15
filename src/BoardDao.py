from src.constants import Constants

__author__ = 'Vijaya'

from dal import DBFactory
from couchquery import Database
import json

class BoardDao:

    @staticmethod
    def createboard(board, userid):
        try:
            doc = BoardDao.getUserDoc(userid)
            if Constants.BOARDS not in doc:
                doc.boards = []
            doc.boards.append(board)
            DBFactory.getdb().updateDoc(doc)
        except:
            raise

    @staticmethod
    def updateBoard(id, boardName, newBoard):
        try:
            doc = BoardDao.getUserDoc(id)
            boards = doc.boards
            for board in boards:
                    if board[Constants.BOARDNAME].lower() == boardName:
                        board[Constants.BOARDNAME] = newBoard[Constants.BOARDNAME]
                        board[Constants.BOARD_DESC] = newBoard[Constants.BOARD_DESC]
                        board[Constants.CATEGORY] = newBoard[Constants.CATEGORY]
                        board[Constants.ISPRIVATE] = newBoard[Constants.ISPRIVATE]
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
                if boards[index][Constants.BOARDNAME].lower() == boardName:
                    boards.pop(index)
                    DBFactory.getdb().updateDoc(doc)
                    return
        except:
            raise

    @staticmethod
    def getUserboards(id):
        msg = BoardDao.getUserDoc(id)
        if Constants.BOARDS in msg:
            return msg.boards
        return Constants.boards_empty_error

    @staticmethod
    def getBoardDetails(id, boardName):
        try:
            boardName = boardName.replace('-', ' ')
            boards = BoardDao.getUserboards(id)
            for board in boards:
                if board[Constants.BOARDNAME].lower() == boardName:
                    return board
        except:
            raise