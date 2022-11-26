from Handlers.Common.BaseHandler import BaseHandler
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Utility.Enums.MainFlow import MainFlow

class OnboardingHandler(BaseHandler):

    def enableFlow(self, bot, message, flowManager):
        markup = InterfaceManager.generateLanguageSelectionLayout()
        bot.reply_to(message, LocalizationManager.instance().onboarding.botStartMsg, reply_markup=markup)

    def handleCommand(self, bot, message, flowManager):
        if message.text == "English" or message.text == "Русский":
            # to do -- assign language

            LocalizationManager.instance().updateLocalization(message.text)

            # print(LocalizationManager.instance().lang)

            markup = InterfaceManager.generateMainMenuLayout(flowManager)

            bot.reply_to(message, LocalizationManager.instance().onboarding.languageSelectedMsg)
            flowManager.activeFlow = MainFlow.menu
            for x in flowManager.handlers:
                if x.fetchHook() == flowManager.activeFlow.hook():
                    x.enableFlow(bot, message, flowManager)
                    return

            return

    def __init__(self):
        self.flow = MainFlow.onboarding