from ...Model.Classes.Order import Order
from ...Model.Classes.StoreFrontItem import StoreFrontItem
from ...Model.Enums.OrderStatus import OrderStatus
from ...Model.Enums.ClothingType import ClothingType
from typing import List

class SampleDataInstance:
    def fetchUserOrders(self, userID) -> List[Order]:
        item = StoreFrontItem("1", "Кепка бербери блять", "Burburry", ClothingType.accessories, True, 2500, "кепка крутая кто найдет напишите алине", [])
        response = [Order("1", [item], "1", 2500, OrderStatus.completed, "01 Ноября 2022")]
        return response

    def sendCustomerSupportMsg(self, msg):
        return

    def storeSearchTerm(self, term):
        return

    def storeBrowseAll(self, page):
        return
    
    def storeCart(self, storeInteraction, item):
        return

    def storePlaceOrder(self, order):
        return