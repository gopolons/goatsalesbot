from aiogram import types
from Utility.Flows.MainFlow import MainFlow
from Utility.Flows.StoreFlow import StoreFlow
from Utility.Flows.HelpFlow import HelpFlow
from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow

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

    def generateCustomerSupportLayout(customerSupportFlowManager) -> any:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        for x in customerSupportFlowManager.handlers:
            i = x.fetchHook()
            if CustomerSupportFlow.menu.hook() != i:
                item = types.KeyboardButton(i)
                markup.add(item)
            
        mainMenuButton = types.KeyboardButton(MainFlow.menu.hook())
        markup.add(mainMenuButton)

        return markup

    def generateHelpLayout(helpFlowManager) -> any:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        for x in helpFlowManager.handlers:
            i = x.fetchHook() 
            if HelpFlow.menu.hook() != i:
                item = types.KeyboardButton(i)
                markup.add(item)

        mainMenuButton = types.KeyboardButton(MainFlow.menu.hook())
        markup.add(mainMenuButton)

        return markup

    def resetMarkup() -> any:
        markup = types.ReplyKeyboardRemove()
        return markup