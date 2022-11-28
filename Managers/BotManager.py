from aiogram import executor
from Utility.Flows.MainFlow import MainFlow
from .InterfaceManager import InterfaceManager
from .FlowManagers.FlowManager import FlowManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Log.Logging import Logging

# The navigation in the app follows an unbelievably complex and unnecessary but still
# completely functional yet absolutely dimented implementaion of a chain of responsibility
# design pattern. It goes as follows:
#
# There are flows -> flows are FlowManager objects. These objects contain an array which 
# lists all the possible menus that the user can arrive to. The behaviour of said menus 
# is set via the handler objects. Handler objects contain the logic for the given menu
# as well as a set of its own flows if it is a complex menu, such as store.
#
# These flows are controlled via the switchFlow() method. It is the most important 
# piece of logic with regards to navigation. The remaining are handlers for /back 
# and /start commands, and resetToMenu() / sendError() in case these are required.


class BotManager:
    flowManager = FlowManager()

    def setup(self):

        # All possible menu outcomes, fetched from the FlowManager
        handlerHooks = []

        for x in self.flowManager.handlers:
            i = x.fetchHook()
            handlerHooks.append(i)
            
        # Handler for the /start command
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

        # Handler for the /start command
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
        
        # Main navigation logic method
        #
        # This logic reccurs throughout the handlers' own handlers o_O
        # It basically first checks if the text is a familiar command,
        # that it can deduce from the flow manager. If it is, it will
        # 'enable the flow' essentially making the handler active.
        #
        # If it isn't, it will pass down the command to the active handler.
        # The active handler has identical construction on its end, passing 
        # the message down until someone can handle it and return the function.
        #
        # If no none of the handlers can handle a command, the bot returns an error.
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

    # Reset to menu is often used in case the user flow 
    # is stuck, for example after restarting the bot
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

    # Method for sending errors
    async def sendError(self, message):
        await self.bot.send_message(message.from_user.id, LocalizationManager.instance().defaultErr)

    def run(self):
        executor.start_polling(self.dp, skip_updates=True)

    def __init__(self, bot, dp):
        self.bot = bot
        self.dp = dp
        self.logger = Logging.instance().logger
        self.logger.debug("Bot initialised")
        self.setup()
        self.logger.debug("Bot setup complete")
