from Handlers.Store.Helpers.StoreBrowse import StoreBrowse
from Handlers.Store.Helpers.StoreCheckout import StoreCheckout
from Handlers.Store.Helpers.StoreSearch import StoreSearch
from Utility.Enums.StoreFlow import StoreFlow

class StoreFlowManager:
    handlers = [StoreBrowse(), StoreCheckout(), StoreSearch()]
    
    activeFlow = StoreFlow