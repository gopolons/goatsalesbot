from Utility.Flows.StoreFlow import StoreFlow
from ...Common.StoreBaseHandler import StoreBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager
from Managers.InterfaceManager import InterfaceManager

class StoreSearch(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = StoreFlow.search
        markup = InterfaceManager.resetMarkup()
        bot.reply_to(message, LocalizationManager.instance().store.searchMsg, reply_markup=markup)
        return

    def handleCommand(self, bot, message, flowManager):
        # here the search logic will take place
        searchItem = message.text 
        reply = LocalizationManager.instance().store.searchErr
        bot.reply_to(message, reply)
        return

    
    def __init__(self):
        self.storeFlow = StoreFlow.search