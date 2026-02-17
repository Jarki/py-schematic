import logging


def setup_logger(level: str = "DEBUG") -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(asctime)s - [%(levelname)-8s] (%(name)s, %(lineno)d) - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )
    return logging.getLogger()
