import logging

class CustomFormatter(logging.Formatter):
    green = "\033[92m" 
    yellow = "\033[93m" 
    red = "\033[91m"  
    reset = "\033[0m"  

    # Define verbose format with colors
    FORMATS = {
        logging.DEBUG: f"{yellow}[%(levelname)s]{reset}: %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        logging.INFO: f"{green}[%(levelname)s]{reset}: %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        logging.WARNING: f"{yellow}[%(levelname)s]{reset}: %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        logging.ERROR: f"{red}[%(levelname)s]{reset}: %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        logging.CRITICAL: f"{red}[%(levelname)s]{reset}: %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self.reset)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


yellow = "\033[93m"
regular = "\033[0m"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "()": CustomFormatter, 
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "custom",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}