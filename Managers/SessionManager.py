from .BotManager import BotManager
from aiogram import Bot, Dispatcher, executor
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types

class SessionManager:
    botID: str

    def start(self):

        bot = BotManager(self.bot, self.dp)

        bot.run()

    def __init__(self, botID):
        # Initialising the bot and the requisites for BotManager
        self.botID = botID
        self.bot = Bot(token=botID) 
        self.dp = Dispatcher(self.bot, storage = MemoryStorage())