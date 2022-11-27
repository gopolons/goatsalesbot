from telebot import types
from Utility.Enums.MainFlow import MainFlow
from Utility.Enums.StoreFlow import StoreFlow
from Utility.Localization.LocalizationManager import LocalizationManager
from Managers.FlowManagers.StoreFlowManager import StoreFlowManager
from Managers.InterfaceManager import InterfaceManager
from ..Common.BaseHandler import BaseHandler

class StoreHandler(BaseHandler):
    
    storeFlowManager = StoreFlowManager()

    def enableFlow(self, bot, message, flowManager):
        self.storeFlowManager.activeFlow = StoreFlow.menu
        
        markup = InterfaceManager.generateStoreLayout(self.storeFlowManager)
        bot.reply_to(message, LocalizationManager.instance().store.menuMsg, reply_markup=markup)

    def __init__(self):
        self.flow = MainFlow.store

    def handleCommand(self, bot, message, flowManager):
        for x in self.storeFlowManager.handlers:
            if message.text == x.fetchHook():
                self.storeFlowManager.activeFlow = x
                self.storeFlowManager.activeFlow.enableFlow(bot, message, self.storeFlowManager)
                return

            activeFlow = self.storeFlowManager.activeFlow.hook()

            for x in self.storeFlowManager.handlers:
                if activeFlow == x.fetchHook():
                    x.handleCommand(bot, message, self.storeFlowManager)
                    return
        
    
    def checkout(self, bot, message):
        return
