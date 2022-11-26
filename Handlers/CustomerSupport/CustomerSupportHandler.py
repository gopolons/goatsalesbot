from Utility.Enums.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler

class CustomerSupportHandler(BaseHandler):
    def enableFlow(self, bot, message, flowManager):
        bot.reply_to(message, "поддержка")

    def handleCommand(self, bot, message, flowManager):
        if message == "search":
            self.search(bot, message)

    def __init__(self):
        self.flow = MainFlow.customerSupport