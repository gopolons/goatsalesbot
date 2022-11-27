from dataclasses import dataclass
from .StoreFrontItem import StoreFrontItem
from ..Enums.OrderStatus import OrderStatus
from typing import List

@dataclass
class Order:
    id: str
    items: List[StoreFrontItem]
    clientId: str
    totalCost: int
    status: OrderStatus
    timestamp: str