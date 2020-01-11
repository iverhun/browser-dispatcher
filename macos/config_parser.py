#!/usr/bin/env python

import logging
import sys
from model import *
from pattern_matcher import PatternMatcher


# create logger
logger = logging.getLogger('config_parser.py')


def _open(config_file):
    yaml.add_constructor('!Config', config_constructor)
    with open(config_file) as fp:
        return yaml.full_load(fp)


def _process(url, config):
    target = config.default_target
    for rule in config.rules:
        if getattr(PatternMatcher, rule.pattern_type)(url, rule.url_pattern):
            target = rule.target
            break

    return '{}\n{}'.format(target.browser, target.profile)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    # url = sys.argv[1]
    # config_file_path = sys.argv[2]

    # TODO: normalize URL (remove trailing slashes, etc)

    url = 'https://gmail.com'
    config_file_path = '../config/browser-config.yml'

    config = _open(config_file_path)
    print(_process(url, config))
