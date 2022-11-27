from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class HelpFlow(Enum):
    us = LocalizationManager.instance().help.us
    store = LocalizationManager.instance().help.store
    tncpp = LocalizationManager.instance().help.tncpp
    menu = LocalizationManager.instance().help.menu

    def hook(self) -> str:
        return self.value