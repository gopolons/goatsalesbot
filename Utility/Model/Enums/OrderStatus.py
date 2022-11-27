from enum import Enum
from Utility.Localization.LocalizationManager import LocalizationManager

class OrderStatus(Enum):
    completed = 0
    failed = 1
    cancelled = 2

    def getString(self):
        if self == OrderStatus.completed:
            return LocalizationManager.instance().general.orderStatusCompleted
        elif self == OrderStatus.failed:
            return LocalizationManager.instance().general.orderStatusFailed
        elif self == OrderStatus.cancelled:
            return LocalizationManager.instance().general.orderStatusCancelled