LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'stream_formatter': {
            'format': '%(asctime)s - [%(levelname)s] (%(name)s, %(lineno)d) - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'stream_formatter',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        '': {
            'handlers': ['stream'],
            'level': 'ERROR',
            'propagate': True
        },
        'src': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
