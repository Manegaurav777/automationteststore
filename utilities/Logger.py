import inspect
import logging


class Logging_Class:
    @staticmethod
    def log_genarator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(r"C:\\Users\\ASUS\\PycharmProjects\\demo_nopcommerce\\Logs\\log.file")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# File
# Format
# file-->format
# add log
# log level

# Debug
# Info
# warning
# error
# critical
