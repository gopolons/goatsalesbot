from Handlers.CustomerSupport.Helpers.GetInTouch import GetInTouch
from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow

class CustomerSupportFlowManager:
    handlers = [GetInTouch()]

    activeFlow = CustomerSupportFlow