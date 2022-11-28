from Utility.Flows.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Managers.FlowManagers.HelpFlowManager import HelpFlowManager
from Utility.Flows.HelpFlow import HelpFlow

class HelpHandler(BaseHandler):

    helpFlowManager = HelpFlowManager()

    async def enableFlow(self, bot, message, flowManager):
        self.helpFlowManager.activeFlow = HelpFlow.menu
        
        markup = InterfaceManager.generateStoreLayout(self.helpFlowManager)
        await bot.send_message(message.from_user.id, LocalizationManager.instance().help.menuMsg, reply_markup=markup)

    async def handleCommand(self, bot, message, flowManager):
        for x in self.helpFlowManager.handlers:
            if message.text == x.fetchHook():
                self.helpFlowManager.activeFlow = x.helpFlow
                await x.enableFlow(bot, message, self.helpFlowManager)
                return

            activeFlow = self.helpFlowManager.activeFlow.hook()

            for x in self.helpFlowManager.handlers:
                if activeFlow == x.fetchHook():
                    await x.handleCommand(bot, message, self.helpFlowManager)
                    return

    def __init__(self):
        self.flow = MainFlow.help