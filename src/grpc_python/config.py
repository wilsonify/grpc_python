import os
import logging

host = "localhost"
port = 32771

logging_dir = "logs"

logging_config_dict = dict(
    version=1,
    formatters={
        "simple": {"format": """%(asctime)s %(name)-12s %(levelname)-8s %(message)s"""}
    },
    handlers={
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(logging_dir, "rabbit_python.log"),
            "formatter": "simple",
        },
    },
    root={"handlers": ["console", "file"], "level": logging.DEBUG},
)
