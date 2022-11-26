from Utility.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Managers.InterfaceManager import InterfaceManager

class MenuHandler(BaseHandler):
    def enableFlow(self, bot, message, flowManager):
        markup = InterfaceManager.generateMainMenuLayout(flowManager)
        bot.reply_to(message, "Ты в меню, че хочешь", reply_markup=markup)

    def handleCommand(self, bot, message, flowManager):
        if message == "search":
            self.search(bot, message)

    def __init__(self):
        self.flow = MainFlow.menu