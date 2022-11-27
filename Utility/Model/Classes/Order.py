class Order:
    def __init__(self, id, items, clientId, totalCost, orderStatus):
        self.id = id
        self.items = items
        self.clientId = clientId
        self.totalCost = totalCost
        self.orderStatus = orderStatus
