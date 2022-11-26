from Utility.Enums.StoreFlow import StoreFlow

class StoreBaseHandler:
    storeFlow: StoreFlow

    def fetchHook(self) -> str:
        return self.storeFlow.hook()