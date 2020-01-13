#!/usr/bin/env python

import logging
import sys
from model import *
from pattern_matcher import PatternMatcher


# create logger
logger = logging.getLogger('browser_resolver.py')


def load_yaml_config(config_file):
    yaml.add_constructor('!Config', config_constructor)
    with open(config_file) as fp:
        return yaml.full_load(fp)


def process(url, config):
    target = config.default_target
    for rule in config.rules:
        if getattr(PatternMatcher, rule.pattern_type)(url, rule.url_pattern):
            target = rule.target
            break

    return target


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    url = sys.argv[1]
    config_file_path = sys.argv[2]

    # TODO: normalize URL (remove trailing slashes, etc)

    config = load_yaml_config(config_file_path)

    print(process(url, config))
