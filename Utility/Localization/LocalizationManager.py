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
    searchMsg = str
    browseMsg = str
    checkoutMsg = str

    # errors
    searchErr = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.menuMsg = """Магазин. Выберите опцию:
🔍 - Поиск
👀 - Смотреть новинки
💸 - Оплата
⬅️ - Главное меню
            """
            self.searchMsg = "Какую вещь вы ищете? Напишите название бренда, вещи, или категории (обувь, верхняя одежда итд)"
            self.browseMsg = "Здесь вы можете ознакомиться с коллекциями одежды доступной у нас на платформе"
            self.checkoutMsg = "Здесь вы можете оформить заказ и перейти к оплате"

            self.searchErr = "К сожалению ничего нет по вашему запросу. Пожалуйста попробуйте другое, или напишите /back чтобы вернуться в меню магазина"
            
        
        elif language == "English":

            self.menuMsg = """Store. Pick an option:
🔍 - Search
👀 - Browse collection
💸 - Checkout
⬅️ - Main menu
            """
            self.searchMsg = "What kind of item are you looking for? Write the name of the brand, item, or it's category (shoes, tops etc)"
            self.browseMsg = "Here you can browse our available collections"
            self.checkoutMsg = "Here you can make an order and complete your payment"
           
            self.searchErr = "Unfortunately, nothing was found based on your request. Please try another search term, or send /back to return to shop menu"


    def __init__(self):
        self.updateLocalization("English")
        
class HelpLocalization:
     # commands
    us = "🌟"
    store = "💲"
    tncpp = "©️"
    menu = "⬅️"

    # messages
    menuMsg = str
    storeMsg = str
    TNCPPMsg = str
    usMsg = str
    
    def updateLocalization(self, language):
        if language == "Русский":

            self.menuMsg = """Помощь. Выберите опцию:
🌟 - О нас
💲 - О магазине
©️ - Политика конфиденциальности
⬅️ - Главное меню
            """
            self.storeMsg = "Описание работы магазины"
            self.TNCPPMsg = "Политика пользования // Политика конфеденциальности"
            self.usMsg = "О нас"
            
        elif language == "English":

            self.menuMsg = """Help. Select an option:
🌟 - About us
💲 - About store
©️ - Privacy policy
⬅️ - Main menu
            """
            self.storeMsg = "Description of how store works"
            self.TNCPPMsg = "PP // TNC text"
            self.usMsg = "About us"

    def __init__(self):
        self.updateLocalization("English")

class OnboardingLocalization:

    # messages
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
    def updateLocalization(self, language):
        return

    def __init__(self):
        self.updateLocalization("English")

class MyOrdersLocalization:

    # messages
    menuMsg = str

    # errors
    noOrdersErr = str
    fetchErr = str

    def updateLocalization(self, language):
        if language == "Русский":
            self.menuMsg = "История ваших заказов:"

            self.noOrdersErr = "У вас еще нет заказов! Перейдите в магазин 🛒 чтобы ознакомиться с коллекцией и оформить ваш первый заказ"
            self.fetchErr = "Ошибка при поиске заказов. Пожалуйста попробуйте снова"

        elif language == "English":
            self.menuMsg = "Your order history:"

            self.noOrdersErr = "You don't have any orders yet! Go to the store 🛒 to browse the collection and place your first order"
            self.fetchErr = "Error when fetching orders. Please try again"

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
    sessionExpiredErr = str

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
            self.sessionExpiredErr = "Your session has expired. Please try again"

        elif language == "Русский":
            
            # err
            self.defaultErr = "Неизвестная ошибка. Проверьте введенные данные"
            self.sessionExpiredErr = "Ваша сессия закончилась. Пожалуйста попробуйте снова"


    def __init__(self):
        self.updateLocalization("English")