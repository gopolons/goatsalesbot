from Utility.Flows.MainFlow import MainFlow
from ..Common.BaseHandler import BaseHandler
from Managers.FlowManagers.CustomerSupportFlowManager import CustomerSupportFlowManager
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager
from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow

class CustomerSupportHandler(BaseHandler):

    customerSupportFlowManager = CustomerSupportFlowManager

    def enableFlow(self, bot, message, flowManager):
        self.customerSupportFlowManager.activeFlow = CustomerSupportFlow.menu

        markup = InterfaceManager.generateCustomerSupportLayout(self.customerSupportFlowManager)
        bot.reply_to(message, LocalizationManager.instance().customerSupport.menuMsg, reply_markup=markup)

    def handleCommand(self, bot, message, flowManager):
        for x in self.customerSupportFlowManager.handlers:
            if message.text == x.fetchHook():
                self.customerSupportFlowManager.activeFlow = x.customerSupportFlow
                x.enableFlow(bot, message, self.customerSupportFlowManager)
                return

            activeFlow = self.customerSupportFlowManager.activeFlow.hook()

            for x in self.customerSupportFlowManager.handlers:
                if activeFlow == x.fetchHook():
                    x.handleCommand(bot, message, self.customerSupportFlowManager)
                    return

    def __init__(self):
        self.flow = MainFlow.customerSupport