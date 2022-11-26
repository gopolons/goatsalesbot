from Utility.StoreFlow import StoreFlow
from ..Common.StoreBaseHandler import StoreBaseHandler

class StoreBrowse(StoreBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        bot.reply_to(message, "тут будут шмоточки которые по горячим скидочкам")
        return
    
    def __init__(self):
        self.storeFlow = StoreFlow.browse