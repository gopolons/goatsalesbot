import telebot
from telebot import types
from Utility.Enums.MainFlow import MainFlow
from .InterfaceManager import InterfaceManager
from .FlowManagers.FlowManager import FlowManager
from Utility.Localization.LocalizationManager import LocalizationManager

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
            self.flowManager.activeFlow = MainFlow.onboarding
        
            msgcom = MainFlow.onboarding.value


            for x in self.flowManager.handlers:
                i = x.fetchHook()

                print(msgcom)
                print(i)

                if i == msgcom:
                    self.flowManager.activeFlow = x.flow
                    x.enableFlow(self.bot, message, self.flowManager)
                    return

            return

        @self.bot.message_handler(regexp="[А-яA-z]")
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

                msgcom = self.flowManager.activeFlow.hook()
                
                if i == msgcom:
                    x.handleCommand(self.bot, message, self.flowManager)
                    return


            self.sendError(message)
            return

            
    def sendError(self, message):
        self.bot.reply_to(message, LocalizationManager.instance().defaultError)

    def run(self):
        self.bot.infinity_polling()

    def __init__(self, botToken):
        self.botToken = botToken
        self.bot = telebot.TeleBot(botToken, parse_mode=None) 
        self.setup()
