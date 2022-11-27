from Utility.Enums.HelpFlow import HelpFlow
from ...Common.HelpBaseHandler import HelpBaseHandler

class HelpUs(HelpBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = HelpFlow.menu
        bot.reply_to(message, "тут будет написано про нас")
        return

    def __init__(self):
        self.helpFlow = HelpFlow.us