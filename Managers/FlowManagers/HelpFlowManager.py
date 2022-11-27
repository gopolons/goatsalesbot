from Handlers.Help.Helpers.HelpStore import HelpStore
from Handlers.Help.Helpers.HelpTNCPP import HelpTNCPP
from Handlers.Help.Helpers.HelpUs import HelpUs
from Utility.Flows.HelpFlow import HelpFlow

class HelpFlowManager:
    handlers = [HelpStore(), HelpTNCPP(), HelpUs()]

    activeFlow = HelpFlow