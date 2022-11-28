import logging
from logging import Logger
from Utility.Singleton import Singleton

@Singleton
class Logging:

    logger = Logger
    
    def __init__(self):
        self.logger = logging.getLogger('MAIN')
        self.logger.setLevel(logging.DEBUG)
        
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.ch.setFormatter(formatter)

        self.logger.addHandler(self.ch)

        # Different messages that can be presented via the logger. The event is logged depending
        # on the level of its importance and levels of StreamHandler & Logger itself

        # self.logger.debug('debug message')
        # self.logger.info('info message')
        # self.logger.warning('warn message')
        # self.logger.error('error message')
        # self.logger.critical('critical message')