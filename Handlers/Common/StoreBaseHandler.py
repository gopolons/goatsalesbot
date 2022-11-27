from Utility.Flows.StoreFlow import StoreFlow

class StoreBaseHandler:
    def fetchHook(self) -> str:
        return self.storeFlow.hook()

    def __init__(self):
        self.storeFlow = StoreFlow