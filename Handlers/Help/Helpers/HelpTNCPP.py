from Utility.Enums.HelpFlow import HelpFlow
from ...Common.HelpBaseHandler import HelpBaseHandler

class HelpTNCPP(HelpBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = HelpFlow.menu
        bot.reply_to(message, "тут будут всякие tnc ништяки")
        return

    def __init__(self):
        self.helpFlow = HelpFlow.tncpp