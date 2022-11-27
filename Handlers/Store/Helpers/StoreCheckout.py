from Utility.Enums.StoreFlow import StoreFlow
from ...Common.StoreBaseHandler import StoreBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager

class StoreCheckout(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = StoreFlow.menu
        bot.reply_to(message, LocalizationManager.instance().store.checkoutMsg)
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.checkout