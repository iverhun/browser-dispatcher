#!/usr/bin/env python

import logging.config
import os
from os import path
import sys

from application import Application


def _settings():
    if os.getenv("DEV"):
        return path.join('../config/browser-config.yml'), path.join('logging.conf')

    return path.join(os.getenv("HOME"), '.browser-dispatcher', 'config.yml'), \
           path.join(os.getenv("HOME"), '.browser-dispatcher', 'logging.conf')


def main():
    config_file, logging_config_file = _settings()

    logging.config.fileConfig(logging_config_file)
    try:
        Application(config_file).run(sys.argv[1])
    except Exception as e:
        logging.critical(e, exc_info=True)


if __name__ == "__main__":
    main()
