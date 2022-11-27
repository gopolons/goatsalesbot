from ...Common.CustomerSupportBaseHandler import CustomerSupportBaseHandler
from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager

class GetInTouch(CustomerSupportBaseHandler):

    def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = CustomerSupportFlow.getInTouch
        markup = InterfaceManager.resetMarkup()
        bot.reply_to(message, LocalizationManager.instance().customerSupport.instructionMsg, reply_markup=markup)
        return

    def handleCommand(self, bot, message, flowManager):
        # here the get in touch logic will take place
        msg = message.text 
        reply = LocalizationManager.instance().customerSupport.submissionMsg
        bot.reply_to(message, reply)

    def __init__(self):
        self.customerSupportFlow = CustomerSupportFlow.getInTouch
