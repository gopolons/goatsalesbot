from Handlers.Common.BaseHandler import BaseHandler
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Utility.Flows.MainFlow import MainFlow

class OnboardingHandler(BaseHandler):

    async def enableFlow(self, bot, message, flowManager):
        markup = InterfaceManager.generateLanguageSelectionLayout()
        await bot.send_message(message.from_user.id, LocalizationManager.instance().onboarding.botStartMsg, reply_markup=markup)

    async def handleCommand(self, bot, message, flowManager):
        if message.text == "English" or message.text == "Русский":

            LocalizationManager.instance().updateLocalization(message.text)

            markup = InterfaceManager.generateMainMenuLayout(flowManager)

            await bot.send_message(message.from_user.id, LocalizationManager.instance().onboarding.languageSelectedMsg)
            flowManager.activeFlow = MainFlow.menu
            for x in flowManager.handlers:
                if x.fetchHook() == flowManager.activeFlow.hook():
                    await x.enableFlow(bot, message, flowManager)
                    return

            return

    def __init__(self):
        self.flow = MainFlow.onboarding