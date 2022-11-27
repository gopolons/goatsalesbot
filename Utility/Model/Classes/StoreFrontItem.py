from dataclasses import dataclass
from typing import List
from ..Enums.ClothingType import ClothingType

@dataclass
class StoreFrontItem:
    id: str
    name: str
    brand: str
    type: ClothingType
    active: bool
    cost: int
    description: str
    images: List[str]
        