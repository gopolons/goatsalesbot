from Managers.SessionManager import SessionManager
from Log.Logging import Logging

logger = Logging.instance()
logger.logger.debug("___GOSHANOTE___")
logger.logger.debug("APP STARTED")

session = SessionManager("5914085904:AAEe1Pyu9DlT4SHWKIeVamoJ4yj65Mxbrok")

session.start()