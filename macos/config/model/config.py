import yaml


class Config(yaml.YAMLObject):
    yaml_tag = '!Config'

    def __init__(self, default_target=None, targets=None, rules=None):
        self.default_target = default_target
        self.targets = targets
        self.rules = rules

    def __str__(self):
        return "Config(default-target: %s)" % self.default_target

