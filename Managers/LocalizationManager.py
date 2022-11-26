class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

@Singleton
class LocalizationManager:
    lang = "Русский"
    
    botStartMsg = str
    
    # main menu options
    
    menu = str
    store = str
    customerSupport = str
    myOrders = str
    help = str
    localization = str

    # main menu messages

    menuMsg = str

    # store menu options

    search = str
    browse = str
    checkout = str
    storeMenu = str

    # store menu messages

    storeMsg = str

    # err

    defaultErr = str

    def updateLocalization(self, language):
        self.lang = language

        if language == "English":
            self.botStartMsg = "Welcome. Please select a language"

            # main menu options
            self.menu = "Main menu"
            self.store = "Store"
            self.customerSupport = "Customer Support"
            self.myOrders = "My orders"
            self.help = "Help"
            self.localization = "Language selection"

            # main menu messages
            self.menuMsg = "Main menu. Pick an option"

            # store options
            self.search = "Search"
            self.browse = "Browse"
            self.checkout = "Checkout"
            self.storeMenu = "Menu"

            # store menu messages
            self.storeMsg = "Store. Pick an option"

            # err
            self.defaultErr = "Unknown error. Please check your data"

        elif language == "Русский":
            self.botStartMsg = "Добро пожаловать. Выберите язык"

            # main menu options
            self.menu = "Главное меню"
            self.store = "Магазин"
            self.customerSupport = "Поддержка"
            self.myOrders = "Мои заказы"
            self.help = "Помощь"
            self.localization = "Выбор языка"

            # main menu messages
            self.menuMsg = "Главное меню. Выберите опцию"

            # store options
            self.search = "Поиск"
            self.browse = "Новинки"
            self.checkout = "Оплата"
            self.storeMenu = "Меню"

            # store menu messages
            self.storeMsg = "Магазин. Выберите опцию"

            # err
            self.defaultErr = "Неизвестная ошибка. Проверьте введенные данные"