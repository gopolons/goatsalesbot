from Utility.Flows.StoreFlow import StoreFlow
from ...Common.StoreBaseHandler import StoreBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager

class StoreCheckout(StoreBaseHandler):

    async def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = StoreFlow.menu
        await bot.send_message(message.from_user.id, LocalizationManager.instance().store.checkoutMsg)
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.checkout