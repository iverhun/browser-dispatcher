import yaml

from .model.rule import Rule, HostsRule, BaseRule
from .model.target import Target
from .model.config import Config
from .pattern_matcher import PatternMatcher
from osascripts import osa


def _rule_constructor(props):
    if props.get('hosts', None):
        return HostsRule(props)
    else:
        return Rule(props)


def _config_constructor(loader, node):
    objects = loader.construct_mapping(node, deep=True)
    rules = map(_rule_constructor, _get_or_default(objects, 'rules', []))
    targets = map(Target, objects['targets'])
    return Config(Target(objects['default_target']), targets, rules)


def _get_or_default(dict, key, default):
    """
    :param dict: the dictionary to look up in
    :param key: the key to look up
    :param default: the value to return if the key doesn't exist ot if it's value is None
    :return: value mapped by the key if the key exists and the value is no None. default otherwise.
    """
    if key in dict.keys():
        return dict.get(key) if dict.get(key) is not None else default
    else:
        return default


class ConfigProcessor:

    def __init__(self, config_file):
        yaml.add_constructor(Config.yaml_tag, _config_constructor)
        with open(config_file) as fp:
            self.config: Config = yaml.full_load(fp)

    def _select_profile(self, target: Target):
        profiles = map(lambda t: "{} - {}".format(t.browser, t.profile), self.config.targets)
        return target if not target.select_profile else osa.read_profile_selector_dialog('osascripts/choose.scpt', profiles)

    def target(self, url):
        for rule in self.config.rules:
            if rule.apply(url, getattr(PatternMatcher, rule.pattern_type)):
                return self._select_profile(rule.target)

        # TODO: if the rule says to show profile selector dialog....
        # TODO: ...

        return self._select_profile(self.config.default_target)
