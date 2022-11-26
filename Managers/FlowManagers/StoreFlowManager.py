from Handlers.Store.StoreBrowse import StoreBrowse
from Handlers.Store.StoreCheckout import StoreCheckout
from Handlers.Store.StoreSearch import StoreSearch
from Utility.StoreFlow import StoreFlow

class StoreFlowManager:
    handlers = [StoreBrowse(), StoreCheckout(), StoreSearch()]
    
    activeFlow = StoreFlow