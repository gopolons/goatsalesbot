from telebot import types
from Utility.Enums.MainFlow import MainFlow
from Utility.Enums.StoreFlow import StoreFlow

class InterfaceManager:
    def generateLanguageSelectionLayout() -> any:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        english = types.KeyboardButton("English")
        russian = types.KeyboardButton("Русский")
        markup.add(english, russian)

        return markup

    def generateMainMenuLayout(flowManager) -> any:
        markup = types.ReplyKeyboardMarkup(row_width=2)  
        for x in flowManager.handlers:
            i = x.fetchHook()
            if MainFlow.menu.hook() != i:
                item = types.KeyboardButton(i)
                markup.add(item)

        return markup

    def generateStoreLayout(storeFlowManager) -> any:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        for x in storeFlowManager.handlers:
            i = x.fetchHook()
            if StoreFlow.menu.hook() != i:
                item = types.KeyboardButton(i)
                markup.add(item)
            
        mainMenuButton = types.KeyboardButton(MainFlow.menu.hook())
        markup.add(mainMenuButton)

        return markup

    def resetMarkup() -> any:
        markup = types.ReplyKeyboardRemove()
        return markup