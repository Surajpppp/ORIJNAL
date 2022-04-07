import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s:    %(levelname)s:    %(message)s', force=True)
        logger = logging.getLogger('ssss')
        logger.setLevel(logging.DEBUG)
        return logger