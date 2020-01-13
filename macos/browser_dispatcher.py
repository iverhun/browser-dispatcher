#!/usr/bin/env python

import logging
import sys

from config.config_processor import ConfigProcessor

# create logger
logger = logging.getLogger('browser_dispatcher')


def execute(target, url):
    print target
    print url
    # os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory=\"{}\" \"{}\" >> /dev/null &".format(target.profile, url))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    url = sys.argv[1]
    config_file_path = sys.argv[2]

    config = ConfigProcessor(config_file_path)
    target = config.target(url)

    execute(target, url)
