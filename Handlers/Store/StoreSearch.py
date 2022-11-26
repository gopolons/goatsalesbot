from Utility.Enums.StoreFlow import StoreFlow
from ..Common.StoreBaseHandler import StoreBaseHandler

class StoreSearch(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        bot.reply_to(message, "тут будет поиск")
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.search