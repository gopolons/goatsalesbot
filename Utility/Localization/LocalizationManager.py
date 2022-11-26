from Utility.Singleton import Singleton

class MainMenuLocalization:
    # commands
    menu = "⬅️"
    store = "🛒"
    customerSupport = "📞"
    myOrders = "🗒️"
    help = "❓"
    onboarding = "🌎"

    # messages
    menuMsg = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.menuMsg = """Главное меню. Выберите опцию:
🛒 - Перейти в магазин
📞 - Служба поддержки
🗒️ - Мои заказы
❓ - Помощь
🌎 - Выбор языка
            """
        
        elif language == "English":

            self.menuMsg = """Main menu. Pick an option:
🛒 - Shop
📞 - Customer support
🗒️ - My orders
❓ - Help
🌎 - Select language
            """

    def __init__(self):
        self.updateLocalization("English")

class StoreLocalization:
    # commands
    search = "🔍"
    browse = "👀"
    checkout = "💸"
    menu = "⬅️"

    # messages
    menuMsg = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.menuMsg = """Магазин. Выберите опцию:
🔍 - Поиск
👀 - Смотреть новинки
💸 - Оплата
⬅️ - Главное меню
            """
        
        elif language == "English":

            self.menuMsg = """Store. Pick an option:
🔍 - Search
👀 - Browse collection
💸 - Checkout
⬅️ - Main menu
            """

    def __init__(self):
        self.updateLocalization("English")
        
class HelpLocalization:
    lang = "Русский"
    
    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

class OnboardingLocalization:
    botStartMsg = str
    
    languageSelectedMsg = str

    def updateLocalization(self, language):
        if language == "Русский":
            self.botStartMsg = "Добро пожаловать. Выберите язык"
            self.languageSelectedMsg = "Язык выбран"
        elif language == "English":
            self.botStartMsg = "Welcome. Select the language"
            self.languageSelectedMsg = "Language selected"

    def __init__(self):
        self.updateLocalization("English")

class CustomerSupportLocalization:
    lang = "Русский"
    
    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

class MyOrdersLocalization:
    lang = "Русский"

    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

@Singleton
class LocalizationManager:
    lang = "Русский"

    # localization objects
    mainMenu = MainMenuLocalization()
    store = StoreLocalization()
    help = HelpLocalization()
    onboarding = OnboardingLocalization()
    customerSupport = CustomerSupportLocalization()
    myOrders = MyOrdersLocalization()

    defaultErr = str

    def updateLocalization(self, language):
        self.lang = language

        self.mainMenu.updateLocalization(language)
        self.store.updateLocalization(language)
        self.help.updateLocalization(language)
        self.onboarding.updateLocalization(language)
        self.customerSupport.updateLocalization(language)
        self.myOrders.updateLocalization(language)

        if language == "English":

            # err
            self.defaultErr = "Unknown error. Please check your data"

        elif language == "Русский":
            
            # err
            self.defaultErr = "Неизвестная ошибка. Проверьте введенные данные"


    def __init__(self):
        self.updateLocalization("English")