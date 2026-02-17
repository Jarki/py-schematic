import logging

import src
from src.settings import settings


def main() -> None:
    src.setup_logger(settings.log_level)

    logger = logging.getLogger(__name__)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    print("Hello from New schematic!")


if __name__ == "__main__":
    main()
