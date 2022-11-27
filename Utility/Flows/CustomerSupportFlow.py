from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class CustomerSupportFlow(Enum):
    getInTouch = LocalizationManager.instance().customerSupport.getInTouch
    menu = LocalizationManager.instance().help.menu

    def hook(self) -> str:
        return self.value