from Managers.SessionManager import SessionManager
from Log.Logging import Logging

# App initialised here
# 
# Session manager is an object used to manage a current session. When the instance is running it will log 
# errors and other certain events into the console. You can control that behavior via Logging.

if __name__ == "__main__":
    logger = Logging.instance()
    logger.logger.debug("__GOATSALES2022__")
    logger.logger.debug("APP STARTED")

    session = SessionManager("5914085904:AAEe1Pyu9DlT4SHWKIeVamoJ4yj65Mxbrok")

    session.start() 

