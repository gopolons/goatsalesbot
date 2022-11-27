from Utility.Enums.StoreFlow import StoreFlow
from ...Common.StoreBaseHandler import StoreBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager

class StoreBrowse(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = StoreFlow.menu
        bot.reply_to(message, LocalizationManager.instance().store.browseMsg)
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.browse