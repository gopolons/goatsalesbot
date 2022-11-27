import telebot
from telebot import types
from Utility.Enums.MainFlow import MainFlow
from .InterfaceManager import InterfaceManager
from .FlowManagers.FlowManager import FlowManager
from Utility.Localization.LocalizationManager import LocalizationManager
from System.Logging import Logging

class BotManager:
    botToken = ""

    bot: telebot = any

    flowManager = FlowManager()

    def setup(self):

        handlerHooks = []

        for x in self.flowManager.handlers:
            i = x.fetchHook()
            handlerHooks.append(i)

        @self.bot.message_handler(commands=["start"])
        def botStart(message):

            self.logger.debug("**__Received a start command from "+ str(message.from_user.id) + "__**")
            self.flowManager.activeFlow = MainFlow.onboarding
        
            msgcom = MainFlow.onboarding.value

            for x in self.flowManager.handlers:
                i = x.fetchHook()

                # print(msgcom)
                # print(i)

                if i == msgcom:
                    self.flowManager.activeFlow = x.flow
                    x.enableFlow(self.bot, message, self.flowManager)
                    return

            return

        @self.bot.message_handler(commands=["back"])
        def back(message):
            try:
                msgcom = self.flowManager.activeFlow.hook()
            except: 
                self.resetToMenu(message)
                return

            for x in self.flowManager.handlers:

                i = x.fetchHook()

                if i == msgcom:
                    x.enableFlow(self.bot, message, self.flowManager)
                    return

        @self.bot.message_handler()
        def switchFlow(message):
            
            msgcom = message.text

            for x in self.flowManager.handlers:

                i = x.fetchHook()
                
                if i == msgcom:
                    self.flowManager.activeFlow = x.flow
                    x.enableFlow(self.bot, message, self.flowManager)
                    return

            for x in self.flowManager.handlers:

                i = x.fetchHook()

                try:
                    msgcom = self.flowManager.activeFlow.hook()
                except: 
                    self.resetToMenu(message)
                    return

                if i == msgcom:
                    x.handleCommand(self.bot, message, self.flowManager)
                    return


            self.sendError(message)
            return

    def resetToMenu(self, message):
        self.logger.debug("**__"+ str(message.from_user.id) + " user session was force reset__**")

        self.bot.reply_to(message, LocalizationManager.instance().sessionExpiredErr)

        self.flowManager.activeFlow = MainFlow.menu

        msgcom = MainFlow.menu.value

        for x in self.flowManager.handlers:
            i = x.fetchHook()

            if i == msgcom:
                self.flowManager.activeFlow = x.flow
                x.enableFlow(self.bot, message, self.flowManager)

    def sendError(self, message):
        self.bot.reply_to(message, LocalizationManager.instance().defaultErr)

    def run(self):
        self.bot.infinity_polling()

    def __init__(self, botToken):
        self.botToken = botToken
        self.bot = telebot.TeleBot(botToken, parse_mode=None) 
        self.logger = Logging.instance().logger
        self.logger.debug("Bot initialised")
        self.setup()
        self.logger.debug("Bot setup complete")
