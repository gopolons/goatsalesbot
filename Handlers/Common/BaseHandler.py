from Utility.MainFlow import MainFlow

class BaseHandler:
    flow: MainFlow

    def fetchHook(self) -> str:
        return self.flow.hook()