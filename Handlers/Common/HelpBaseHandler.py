from Utility.Enums.HelpFlow import HelpFlow

class HelpBaseHandler:
    def fetchHook(self) -> str:
        return self.helpFlow.hook()

    def __init__(self):
        self.helpFlow = HelpFlow