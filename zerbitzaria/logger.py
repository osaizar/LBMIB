import logging
import logging.handlers
import sys

class Logger():

    def __init__(self):
        try:
            self.logger = logging.getLogger("lbmib")
            self.logger.setLevel(logging.DEBUG)

            # create a file handler
            handler = logging.SysLogHandler(address = "/dev/log")

            # create a logging format
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)

            # add the handlers to the logger
            self.logger.addHandler(handler)
        except Exception, e:
            print "[!] Arazoa loggera hastean. Programa irten egingo da!"
            print "[!] "+str(e)
            sys.exit(1)

    def get_logger(self):
        return self.logger
