from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow

class CustomerSupportBaseHandler:
    def fetchHook(self) -> str:
        return self.customerSupportFlow.hook()

    def __init__(self):
        self.customerSupportFlow = CustomerSupportFlow