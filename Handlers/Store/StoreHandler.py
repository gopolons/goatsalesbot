from telebot import types
from Utility.Flows.MainFlow import MainFlow
from Utility.Flows.StoreFlow import StoreFlow
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

    def handleCommand(self, bot, message, flowManager):
        for x in self.storeFlowManager.handlers:
            if message.text == x.fetchHook():
                self.storeFlowManager.activeFlow = x.storeFlow
                x.enableFlow(bot, message, self.storeFlowManager)
                return

            activeFlow = self.storeFlowManager.activeFlow.hook()

            for x in self.storeFlowManager.handlers:
                if activeFlow == x.fetchHook():
                    x.handleCommand(bot, message, self.storeFlowManager)
                    return
        
    def __init__(self):
        self.flow = MainFlow.store
