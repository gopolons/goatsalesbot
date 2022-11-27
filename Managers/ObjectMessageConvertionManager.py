from Utility.Localization.LocalizationManager import LocalizationManager

class ObjectMessageConvertionManager:
    def orderToStr(self, bot, message, orders):
        for order in orders:
            id = order.id
            items = order.items
            clientId = order.clientId
            totalCost = order.totalCost
            status = order.status.getString()
            timestamp = order.timestamp

            itemsString = ""

            count = 0

            for item in items:
                count += 1
                i = f"\n {str(count)}. {item.name}, {item.type.getString()}, {item.cost}"
                itemsString += i

            introStr = LocalizationManager.instance().general.yourOrderFromServ
            priceStr = LocalizationManager.instance().general.priceServ
            statusStr = LocalizationManager.instance().general.statusServ
            
            messageContent = f"""{introStr} {timestamp} {itemsString}
{priceStr} {totalCost}
{statusStr} {status}            
            """

            bot.send_message(message.chat.id, messageContent)
