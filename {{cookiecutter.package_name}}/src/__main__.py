import logging

import src


def main() -> None:
    src.setup_logger()

    logger = logging.getLogger(__name__)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    print("Hello from {{ cookiecutter.project_name }}!")

if __name__ == "__main__":
    main()
