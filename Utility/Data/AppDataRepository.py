from Debug.DebugCases import debug
from Common.DBInterface import DBInterface
from .DS.DatabaseConnector import DatabaseConnector
from .DS.SampleDataInstance import SampleDataInstance

class AppDataRepository:
    dbInterface = DBInterface

    def fetchUserOrders(userID):
        return DBInterface.fetchUserOrders(userID)

    def sendCustomerSupportMsg(msg):
        return DBInterface.sendCustomerSupportMsg(msg)

    def storeSearchTerm(term):
        return DBInterface.storeSearchTerm(term)

    def storeBrowseAll(page):
        return DBInterface.storeBrowseAll(page)
    
    def storeCart(storeInteraction, item):
        return DBInterface.storeCart(storeInteraction, item)

    def storePlaceOrder(order):
        return DBInterface.storePlaceOrder(order)

    def __init__(self):
        if debug:
            self.dbInterface = SampleDataInstance()
            return
        else:
            self.dbInterface = DatabaseConnector()
            return
