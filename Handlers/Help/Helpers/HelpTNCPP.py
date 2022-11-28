from Utility.Flows.HelpFlow import HelpFlow
from ...Common.HelpBaseHandler import HelpBaseHandler
from Utility.Localization.LocalizationManager import LocalizationManager

class HelpTNCPP(HelpBaseHandler):

    async def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = HelpFlow.menu
        await bot.send_message(message.from_user.id, LocalizationManager.instance().help.TNCPPMsg)
        return

    def __init__(self):
        self.helpFlow = HelpFlow.tncpp