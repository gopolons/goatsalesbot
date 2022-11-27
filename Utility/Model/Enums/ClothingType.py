from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class ClothingType(Enum):
    shoes = 0
    sneakers = 1
    accessories = 2

    def getString(self):
        if self == ClothingType.shoes:
            return LocalizationManager.instance().clothingTypes.shoes
        elif self == ClothingType.sneakers:
            return LocalizationManager.instance().clothingTypes.sneakers
        elif self == ClothingType.accessories:
            return LocalizationManager.instance().clothingTypes.accessories