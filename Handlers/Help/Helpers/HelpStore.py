from Utility.Enums.HelpFlow import HelpFlow
from ...Common.HelpBaseHandler import HelpBaseHandler

class HelpStore(HelpBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = HelpFlow.menu
        bot.reply_to(message, "тут будет тутор про магазик")
        return

    def __init__(self):
        self.helpFlow = HelpFlow.store