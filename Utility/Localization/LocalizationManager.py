from Utility.Singleton import Singleton

@Singleton
class MainMenuLocalization:
    # commands
    menu = str
    store = str
    customerSupport = str
    myOrders = str
    help = str
    onboarding = str

    # messages
    menuMsg = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.menu = "Главное меню"
            self.store = "Магазин"
            self.customerSupport = "Поддержка"
            self.myOrders = "Мои заказы"
            self.help = "Помощь"
            self.onboarding = "Выбор языка"

            self.menuMsg = "Главное меню. Выберите опцию"
        
        elif language == "English":

            self.menu = "Main menu"
            self.store = "Store"
            self.customerSupport = "Customer Support"
            self.myOrders = "My orders"
            self.help = "Help"
            self.onboarding = "Language selection"

            self.menuMsg = "Main menu. Pick an option"

    def __init__(self):
        self.updateLocalization("English")


@Singleton
class StoreLocalization:
    # commands
    search = str
    browse = str
    checkout = str
    menu = str

    # messages
    menuMsg = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.search = "Поиск"
            self.browse = "Новинки"
            self.checkout = "Оплата"
            self.menu = "Меню"

            self.menuMsg = "Магазин. Выберите опцию"

        elif language == "English":

            self.search = "Search"
            self.browse = "Browse"
            self.checkout = "Checkout"
            self.menu = "Menu"

            self.menuMsg = "Store. Pick an option"

    def __init__(self):
        self.updateLocalization("English")
        

@Singleton
class HelpLocalization:
    lang = "Русский"
    
    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

@Singleton
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

@Singleton
class CustomerSupportLocalization:
    lang = "Русский"
    
    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

@Singleton
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
    mainMenu = MainMenuLocalization.instance()
    store = StoreLocalization.instance()
    help = HelpLocalization.instance()
    onboarding = OnboardingLocalization.instance()
    customerSupport = CustomerSupportLocalization.instance()
    myOrders = MyOrdersLocalization.instance()

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