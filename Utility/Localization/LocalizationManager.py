from Utility.Singleton import Singleton

class MainMenuLocalization:
    # commands
    menu = "⬅️"
    store = "🛒"
    customerSupport = "📞"
    help = "❓"
    myOrders = "🗒️"
    onboarding = "🌎"

    # messages
    menuMsg = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.menuMsg = """Главное меню. Выберите опцию:
🛒 - Перейти в магазин
📞 - Служба поддержки
❓ - Помощь
🗒️ - Мои заказы
🌎 - Выбор языка
            """
        
        elif language == "English":

            self.menuMsg = """Main menu. Pick an option:
🛒 - Shop
📞 - Customer support
❓ - Help
🗒️ - My orders
🌎 - Select language
            """

class StoreLocalization:
    # commands
    browse = "👀"
    checkout = "💸"
    search = "🔍"
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
👀 - Смотреть новинки
💸 - Оплата
🔍 - Поиск
⬅️ - Главное меню
            """
            self.searchMsg = "Какую вещь вы ищете? Напишите название бренда, вещи, или категории (обувь, верхняя одежда итд), или напишите /back чтобы отменить"
            self.browseMsg = "Здесь вы можете ознакомиться с коллекциями одежды доступной у нас на платформе"
            self.checkoutMsg = "Здесь вы можете оформить заказ и перейти к оплате"

            self.searchErr = "К сожалению ничего нет по вашему запросу. Пожалуйста попробуйте другое, или напишите /back чтобы вернуться в меню магазина"
            
        
        elif language == "English":

            self.menuMsg = """Store. Pick an option:
👀 - Browse collection
💸 - Checkout
🔍 - Search
⬅️ - Main menu
            """
            self.searchMsg = "What kind of item are you looking for? Write the name of the brand, item, or it's category (shoes, tops etc), or send /back to cancel"
            self.browseMsg = "Here you can browse our available collections"
            self.checkoutMsg = "Here you can make an order and complete your payment"
           
            self.searchErr = "Unfortunately, nothing was found based on your request. Please try another search term, or send /back to return to shop menu"
        
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
💲 - О магазине
©️ - Политика конфиденциальности
🌟 - О нас
⬅️ - Главное меню
            """
            self.storeMsg = "Описание работы магазины"
            self.TNCPPMsg = "Политика пользования // Политика конфеденциальности"
            self.usMsg = "О нас"
            
        elif language == "English":

            self.menuMsg = """Help. Select an option:
💲 - About store
©️ - Privacy policy
🌟 - About us
⬅️ - Main menu
            """
            self.storeMsg = "Description of how store works"
            self.TNCPPMsg = "PP // TNC text"
            self.usMsg = "About us"

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

class CustomerSupportLocalization:

    # commands
    getInTouch = "✉️"
    menu = "⬅️"

    # messages
    menuMsg = str
    instructionMsg = str
    submissionMsg = str

    def updateLocalization(self, language):
        if language == "Русский":
            self.menuMsg = """Поддержка. Выберите опцию:
✉️ - Связаться
⬅️ - Главное меню
            """
            self.instructionMsg = "Пожалуйста опишите проблему с которой сталкиваетесь. Агент поддержки свяжется с вами лично чтобы помочь. Чтобы отменить, отправьте /back"
            self.submissionMsg = "Спасибо за ваш отзыв! Мы свяжемся с вами как можно скорее. Вы можете оставить еще одно сообщение или нажать /back чтобы вернуться в меню"
        elif language == "English":
            self.menuMsg = """Customer support. Pick an option:
✉️ - Get in touch
⬅️ - Main menu
            """
            self.instructionMsg = "Please describe the problem you're facing. Customer support agent will get in touch to assist you personally. To cancel, send /back"
            self.submissionMsg = "Thank you for your response! We'll get in touch with you as soon as possible. You can leave another message or send /back to dismiss to menu"

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

class GeneralLocalization:

    # types
    orderStatusCompleted = str
    orderStatusCancelled = str
    orderStatusFailed = str

    # service message strings
    yourOrderFromServ = str
    priceServ = str
    statusServ = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.orderStatusCompleted = "Выполнен"
            self.orderStatusCancelled = "Отменен"
            self.orderStatusFailed = "Ошибка"

            self.yourOrderFromServ = "Ваш заказ от"
            self.priceServ = "Цена:"
            self.statusServ = "Статус:"

        elif language == "English":
            
            self.orderStatusCompleted = "Completed"
            self.orderStatusCancelled = "Cancelled"
            self.orderStatusFailed = "Error"

            self.yourOrderFromServ = "Your order from"
            self.priceServ = "Price:"
            self.statusServ = "Status:"

class ClothingTypes:

    # types
    shoes = str
    sneakers = str
    accessories = str

    def updateLocalization(self, language):
        if language == "Русский":

            self.shoes = "Ботинки"
            self.sneakers = "Кроссовки"
            self.accessories = "Аксессуары"

        elif language == "English":
            
            self.shoes = "Shoes"
            self.sneakers = "Sneakers"
            self.accessories = "Accessories"

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
    
    general = GeneralLocalization()
    clothingTypes = ClothingTypes()

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

        self.general.updateLocalization(language)
        self.clothingTypes.updateLocalization(language)

        if language == "Русский":

            # err
            self.defaultErr = "Неизвестная ошибка. Проверьте введенные данные"
            self.sessionExpiredErr = "Ваша сессия закончилась. Пожалуйста попробуйте снова"

        elif language == "English":
            
            # err
            self.defaultErr = "Unknown error. Please check your data"
            self.sessionExpiredErr = "Your session has expired. Please try again"

    def __init__(self):
        self.updateLocalization("Русский")