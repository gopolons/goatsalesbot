from enum import Enum
from Managers.LocalizationManager import LocalizationManager

class MainFlow(Enum):
    menu = "Главное меню"
    store = "Магазин"
    customerSupport = "Поддержка"
    myOrders = "Мои заказы"
    help = "Помощь"
    localization = "Выбор языка"

    def hook(self) -> str:
        return self.value