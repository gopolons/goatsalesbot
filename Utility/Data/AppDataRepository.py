from ..Debug.DebugCases import debug
from .DS.DatabaseConnector import DatabaseConnector
from .DS.SampleDataInstance import SampleDataInstance
from ..Model.Classes.Order import Order
from typing import List

class AppDataRepository:
    dbInterface = any

    def fetchUserOrders(self, userID) -> List[Order]:
        return self.dbInterface.fetchUserOrders(userID)

    def sendCustomerSupportMsg(self, msg):
        return self.dbInterface.sendCustomerSupportMsg(msg)

    def storeSearchTerm(self, term):
        return self.dbInterface.storeSearchTerm(term)

    def storeBrowseAll(self, page):
        return self.dbInterface.storeBrowseAll(page)
    
    def storeCart(self, storeInteraction, item):
        return self.dbInterface.storeCart(storeInteraction, item)

    def storePlaceOrder(self, order):
        return self.dbInterface.storePlaceOrder(order)

    def __init__(self):
        if debug:
            self.dbInterface = SampleDataInstance()
            return
        else:
            self.dbInterface = DatabaseConnector()
            return
