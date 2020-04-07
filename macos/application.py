import logging.config
import os
from os import path

from browser.browsers import browser
from config.config_processor import ConfigProcessor


class Application:

    def __init__(self, config_file):
        logging.getLogger('application').info("Config file: %s" % config_file)
        Application._init(config_file)
        self.config = ConfigProcessor(config_file)

    @staticmethod
    def _init(config_file):
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
        if not path.exists(config_file):
            os.makedirs(os.path.dirname(config_file), exist_ok=True)
            with open(config_file, "w") as f:
                f.write(default_config)

    def run(self, url):
        target = self.config.target(url)
        logging.getLogger('history').info("open: %s\t\turl: %s" % (target, url))
        command_to_execute = browser(target, url).command()
        logging.getLogger('application').info(command_to_execute)

        return os.system(command_to_execute)
