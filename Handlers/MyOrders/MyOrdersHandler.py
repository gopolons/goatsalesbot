from ast import List
from Utility.Flows.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager
from Utility.Model.Classes.Order import Order
from Managers.ObjectMessageConvertionManager import ObjectMessageConvertionManager

class MyOrdersHandler(BaseHandler):
    def enableFlow(self, bot, message, flowManager):
        orders = self.fetchOrders(message.from_user.id)
        if orders == []:
            bot.reply_to(message, LocalizationManager.instance().myOrders.noOrdersErr)
        else:
            bot.reply_to(message, LocalizationManager.instance().myOrders.menuMsg)
            ObjectMessageConvertionManager().orderToStr(bot, orders)
        
    def fetchOrders(self, userID):
        # here the fetch order logic will take place
        return []

    def handleCommand(self, bot, message, flowManager):
        if message == "search":
            self.search(bot, message)

    def __init__(self):
        self.flow = MainFlow.myOrders