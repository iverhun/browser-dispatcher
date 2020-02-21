import yaml


class Config(yaml.YAMLObject):
    yaml_tag = '!Config'

    def __init__(self, targets=None, rules=None, defaults=None):
        self.defaults = defaults
        self.targets = targets
        self.rules = rules

    def __str__(self):
        return "Config(defaults: %s)" % self.defaults

