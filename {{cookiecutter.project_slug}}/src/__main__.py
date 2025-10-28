import logging
import logging.config

import src

logging.config.dictConfig(src.LOGGING_CONFIG)
log = logging.getLogger(__name__)

def main():
    log.debug("Debug message")
    log.info("Info message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")
    print("Hello from {{ cookiecutter.project_name }}!")

if __name__ == "__main__":
    main()
