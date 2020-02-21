#!/usr/bin/env python

import logging
import os
from os import path
import sys

from browser.browsers import browser
from browser.chrome import Chrome
from config.config_processor import ConfigProcessor

# create logger
logger = logging.getLogger('browser_dispatcher')

default_config = """!Config
targets:
- &chrome_default
  browser: chrome
  profile: Default

rules:
- url_pattern: "*example.com/*"
  pattern_type: ant
  target: *chrome_default

defaults:
  target: *ff1
"""


def execute(target, url):
    command_to_execute = browser(target, url).command()
    logger.debug(command_to_execute)
    os.system(command_to_execute)


def init():
    config_file = path.join(os.getenv("HOME"), '.browser-dispatcher', 'config.yml')

    if not path.exists(config_file):
        os.makedirs(os.path.dirname(config_file), exist_ok=True)
        with open(config_file, "w") as f:
            f.write(default_config)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    url = sys.argv[1]

    init()
    config = ConfigProcessor(path.join(os.getenv("HOME"), '.browser-dispatcher', 'config.yml'))
    target = config.target(url)

    execute(target, url)
