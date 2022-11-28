from ast import List
from Utility.Flows.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager
from Managers.ObjectMessageConvertionManager import ObjectMessageConvertionManager
from Utility.Data.AppDataRepository import AppDataRepository

class MyOrdersHandler(BaseHandler):
    async def enableFlow(self, bot, message, flowManager):
        orders = self.fetchOrders(message.from_user.id)
        if orders == []:
            await bot.send_message(message.from_user.id, LocalizationManager.instance().myOrders.noOrdersErr)
        else:
            await bot.send_message(message.from_user.id, LocalizationManager.instance().myOrders.menuMsg)
            ObjectMessageConvertionManager().orderToStr(bot, message, orders)
        
    def fetchOrders(self, userID):
        # research - TypeError: object list can't be used in 'await' expression
        # orders = await self.dataRepo.fetchUserOrders(userID)
        return []

    async def handleCommand(self, bot, message, flowManager):
        if message == "search":
            self.search(bot, message)

    def __init__(self):
        self.flow = MainFlow.myOrders
        self.dataRepo = AppDataRepository()