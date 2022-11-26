from enum import Enum
from Managers.LocalizationManager import LocalizationManager

class StoreFlow(Enum):
    search = "Поиск"
    browse = "Новинки"
    checkout = "Оплата"
    menu = "Меню"

    def hook(self) -> str:
        return self.value