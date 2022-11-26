from .BotManager import BotManager

class SessionManager:
    botID: str

    def start(self):
        bot = BotManager(self.botID)

        bot.run()

    def __init__(self, botID):
        self.botID = botID