from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class StoreFlow(Enum):
    search = LocalizationManager.instance().store.search
    browse = LocalizationManager.instance().store.browse
    checkout = LocalizationManager.instance().store.checkout
    menu = LocalizationManager.instance().store.menu

    def hook(self) -> str:
        return self.value