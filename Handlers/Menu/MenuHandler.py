from Utility.Flows.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager

class MenuHandler(BaseHandler):
    async def enableFlow(self, bot, message, flowManager):
        markup = InterfaceManager.generateMainMenuLayout(flowManager)
        await bot.send_message(message.from_user.id, LocalizationManager.instance().mainMenu.menuMsg, reply_markup=markup)

    def handleCommand(self, bot, message, flowManager):
        if message == "search":
            self.search(bot, message)

    def __init__(self):
        self.flow = MainFlow.menu