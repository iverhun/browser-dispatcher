import yaml

from .model.rule import Rule, HostsRule
from .model.target import Target
from .model.config import Config
from .pattern_matcher import PatternMatcher


def _rule_constructor(props):
    if props.get('hosts', None):
        return HostsRule(props)
    else:
        return Rule(props)


def _config_constructor(loader, node):
    objects = loader.construct_mapping(node, deep=True)
    rules = map(_rule_constructor, objects['rules'])
    targets = map(Target, objects['targets'])
    return Config(Target(objects['default_target']), targets, rules)


class ConfigProcessor:

    def __init__(self, config_file):
        yaml.add_constructor(Config.yaml_tag, _config_constructor)
        with open(config_file) as fp:
            self.config = yaml.full_load(fp)

    def target(self, url):
        for rule in self.config.rules:
            if rule.apply(url, getattr(PatternMatcher, rule.pattern_type)):
                return rule.target

        return self.config.default_target
