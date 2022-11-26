from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class MainFlow(Enum):
    menu = LocalizationManager.instance().mainMenu.menu
    store = LocalizationManager.instance().mainMenu.store
    customerSupport = LocalizationManager.instance().mainMenu.customerSupport
    myOrders = LocalizationManager.instance().mainMenu.myOrders
    help = LocalizationManager.instance().mainMenu.help
    onboarding = LocalizationManager.instance().mainMenu.onboarding

    def hook(self) -> str:
        return self.value