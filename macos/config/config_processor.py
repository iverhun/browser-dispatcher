import yaml

from .model.rule import Rule
from .model.target import Target
from .model.config import Config
from .pattern_matcher import PatternMatcher


def _config_constructor(loader, node):
    objects = loader.construct_mapping(node, deep=True)
    rules = map(Rule, objects['rules'])
    targets = map(Target, objects['targets'])
    return Config(Target(objects['default_target']), targets, rules)


class ConfigProcessor:

    def __init__(self, config_file):
        yaml.add_constructor(Config.yaml_tag, _config_constructor)
        with open(config_file) as fp:
            self.config = yaml.full_load(fp)

    def target(self, url):
        target = self.config.default_target
        for rule in self.config.rules:
            if getattr(PatternMatcher, rule.pattern_type)(url, rule.url_pattern):
                target = rule.target
                break
        return target
