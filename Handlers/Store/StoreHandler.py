from aiogram import types
from Utility.Flows.MainFlow import MainFlow
from Utility.Flows.StoreFlow import StoreFlow
from Utility.Localization.LocalizationManager import LocalizationManager
from Managers.FlowManagers.StoreFlowManager import StoreFlowManager
from Managers.InterfaceManager import InterfaceManager
from ..Common.BaseHandler import BaseHandler

class StoreHandler(BaseHandler):
    
    storeFlowManager = StoreFlowManager()

    async def enableFlow(self, bot, message, flowManager):
        self.storeFlowManager.activeFlow = StoreFlow.menu
        
        markup = InterfaceManager.generateStoreLayout(self.storeFlowManager)
        await bot.send_message(message.from_user.id, LocalizationManager.instance().store.menuMsg, reply_markup=markup)

    async def handleCommand(self, bot, message, flowManager):
        for x in self.storeFlowManager.handlers:
            if message.text == x.fetchHook():
                self.storeFlowManager.activeFlow = x.storeFlow
                await x.enableFlow(bot, message, self.storeFlowManager)
                return

            activeFlow = self.storeFlowManager.activeFlow.hook()

            for x in self.storeFlowManager.handlers:
                if activeFlow == x.fetchHook():
                    await x.handleCommand(bot, message, self.storeFlowManager)
                    return
        
    def __init__(self):
        self.flow = MainFlow.store
