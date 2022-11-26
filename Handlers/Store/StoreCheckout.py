from Utility.StoreFlow import StoreFlow
from ..Common.StoreBaseHandler import StoreBaseHandler

class StoreCheckout(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        bot.reply_to(message, "тут будет оплата хз наверное надо будет заказ отображать")
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.checkout