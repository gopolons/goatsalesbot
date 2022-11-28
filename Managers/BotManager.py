import aiogram
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from Utility.Flows.MainFlow import MainFlow
from .InterfaceManager import InterfaceManager
from .FlowManagers.FlowManager import FlowManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Log.Logging import Logging

class BotManager:
    botToken = ""

    bot = any

    flowManager = FlowManager()

    def setup(self):

        handlerHooks = []

        for x in self.flowManager.handlers:
            i = x.fetchHook()
            handlerHooks.append(i)

        @self.dp.message_handler(commands=["start"])
        async def botStart(message):

            self.logger.debug("**__Received a start command from "+ str(message.from_user.id) + "__**")
            self.flowManager.activeFlow = MainFlow.onboarding
        
            msgcom = MainFlow.onboarding.value

            for x in self.flowManager.handlers:
                i = x.fetchHook()

                if i == msgcom:
                    self.flowManager.activeFlow = x.flow
                    await x.enableFlow(self.bot, message, self.flowManager)
                    return

            return

        @self.dp.message_handler(commands=["back"])
        async def back(message):
            try:
                msgcom = self.flowManager.activeFlow.hook()
            except: 
                await self.resetToMenu(message)
                return

            for x in self.flowManager.handlers:

                i = x.fetchHook()

                if i == msgcom:
                    await x.enableFlow(self.bot, message, self.flowManager)
                    return

        @self.dp.message_handler()
        async def switchFlow(message):
            
            msgcom = message.text

            for x in self.flowManager.handlers:

                i = x.fetchHook()
                
                if i == msgcom:
                    self.flowManager.activeFlow = x.flow
                    await x.enableFlow(self.bot, message, self.flowManager)
                    return

            for x in self.flowManager.handlers:

                i = x.fetchHook()

                try:
                    msgcom = self.flowManager.activeFlow.hook()
                except: 
                    await self.resetToMenu(message)
                    return

                if i == msgcom:
                    await x.handleCommand(self.bot, message, self.flowManager)
                    return


            self.sendError(message)
            return

    async def resetToMenu(self, message):
        self.logger.debug("**__"+ str(message.from_user.id) + " user session was force reset__**")

        await self.bot.send_message(message.from_user.id, LocalizationManager.instance().sessionExpiredErr)

        self.flowManager.activeFlow = MainFlow.menu

        msgcom = MainFlow.menu.value

        for x in self.flowManager.handlers:
            i = x.fetchHook()

            if i == msgcom:
                self.flowManager.activeFlow = x.flow
                await x.enableFlow(self.bot, message, self.flowManager)

    async def sendError(self, message):
        await self.bot.send_message(message.from_user.id, LocalizationManager.instance().defaultErr)

    def run(self):
        executor.start_polling(self.dp, skip_updates=True)

    def __init__(self, botToken):
        self.botToken = botToken
        self.bot = Bot(token=botToken) 
        self.dp = Dispatcher(self.bot, storage = MemoryStorage())
        self.logger = Logging.instance().logger
        self.logger.debug("Bot initialised")
        self.setup()
        self.logger.debug("Bot setup complete")
