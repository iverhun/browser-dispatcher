#!/usr/bin/env python

import logging
import sys
import fnmatch
import re
from model import *

# create logger
logger = logging.getLogger('configparser.py')


class PatternMatcher:
    def __init__(self):
        pass

    @staticmethod
    def ant(url, pattern):
        return fnmatch.fnmatch(url, pattern)

    @staticmethod
    def regex(url, pattern):
        return re.match(pattern, url) is not None


def _config_constructor(loader, node):
    objects = loader.construct_mapping(node, deep=True)
    rules = map(Rule, objects['rules'])
    targets = map(TargetSpec, objects['targets'])
    return Config(Target(objects['default_target']), targets, rules)


def _open(config_file):
    yaml.add_constructor('!Config', _config_constructor)
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
    rules = config.rules
    default_target = config.default_target
    print(_process(url, config))
