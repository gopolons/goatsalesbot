from telebot import types
from Utility.MainFlow import MainFlow
from Utility.StoreFlow import StoreFlow
from Managers.FlowManagers.StoreFlowManager import StoreFlowManager
from Managers.InterfaceManager import InterfaceManager
from ..Common.BaseHandler import BaseHandler

class StoreHandler(BaseHandler):
    
    storeFlowManager = StoreFlowManager()

    def enableFlow(self, bot, message, flowManager):
        self.storeFlowManager.activeFlow = StoreFlow.menu
        
        markup = InterfaceManager.generateStoreLayout(self.storeFlowManager)
        bot.reply_to(message, "Ты в магазе, че хочешь", reply_markup=markup)

    def __init__(self):
        self.flow = MainFlow.store

    def handleCommand(self, bot, message, flowManager):
        for x in self.storeFlowManager.handlers:
            if message.text == x.fetchHook():
                self.storeFlowManager.activeFlow = x
                self.storeFlowManager.activeFlow.enableFlow(bot, message, self.storeFlowManager)
                return
    
    def checkout(self, bot, message):
        return
