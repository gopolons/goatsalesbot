from Utility.Enums.MainFlow import MainFlow

class BaseHandler:
    flow: MainFlow

    def fetchHook(self) -> str:
        return self.flow.hook()