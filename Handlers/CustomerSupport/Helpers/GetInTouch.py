from ...Common.CustomerSupportBaseHandler import CustomerSupportBaseHandler
from Utility.Flows.CustomerSupportFlow import CustomerSupportFlow
from Managers.InterfaceManager import InterfaceManager
from Utility.Localization.LocalizationManager import LocalizationManager

class GetInTouch(CustomerSupportBaseHandler):

    async def enableFlow(self, bot, message, flowManager):
        flowManager.activeFlow = CustomerSupportFlow.getInTouch
        markup = InterfaceManager.resetMarkup()
        await bot.send_message(message.from_user.id, LocalizationManager.instance().customerSupport.instructionMsg, reply_markup=markup)
        return

    async def handleCommand(self, bot, message, flowManager):
        # here the get in touch logic will take place
        msg = message.text 
        reply = LocalizationManager.instance().customerSupport.submissionMsg
        await bot.send_message(message.from_user.id, reply)

    def __init__(self):
        self.customerSupportFlow = CustomerSupportFlow.getInTouch
