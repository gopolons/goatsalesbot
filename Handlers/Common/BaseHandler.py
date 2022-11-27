from Utility.Flows.MainFlow import MainFlow

class BaseHandler:
    def fetchHook(self) -> str:
        return self.flow.hook()

    def __init__(self):
        self.flow = MainFlow