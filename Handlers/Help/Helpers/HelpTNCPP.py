from Utility.Enums.HelpFlow import HelpFlow
from ...Common.HelpBaseHandler import HelpBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager

class HelpTNCPP(HelpBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = HelpFlow.menu
        bot.reply_to(message, LocalizationManager.instance().help.TNCPPMsg)
        return

    def __init__(self):
        self.helpFlow = HelpFlow.tncpp