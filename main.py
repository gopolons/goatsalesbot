from Managers.SessionManager import SessionManager
from Log.Logging import Logging

if __name__ == "__main__":
    logger = Logging.instance()
    logger.logger.debug("__GOATSALES2022__")
    logger.logger.debug("APP STARTED")

    session = SessionManager("5914085904:AAEe1Pyu9DlT4SHWKIeVamoJ4yj65Mxbrok")

    session.start() 

