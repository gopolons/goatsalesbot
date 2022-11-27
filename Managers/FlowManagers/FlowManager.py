from Handlers.Menu.MenuHandler import MenuHandler
from Handlers.Store.StoreHandler import StoreHandler
from Handlers.CustomerSupport.CustomerSupportHandler import CustomerSupportHandler
from Handlers.Help.HelpHandler import HelpHandler
from Handlers.Onboarding.OnboardingHandler import OnboardingHandler
from Handlers.MyOrders.MyOrdersHandler import MyOrdersHandler
from Utility.Flows.MainFlow import MainFlow

class FlowManager:
    handlers = [MenuHandler(), StoreHandler(), CustomerSupportHandler(), HelpHandler(), MyOrdersHandler(), OnboardingHandler()]

    activeFlow = MainFlow