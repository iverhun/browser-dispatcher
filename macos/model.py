import yaml


class Config(yaml.YAMLObject):
    yaml_tag = '!Config'

    def __init__(self, default_target=None, targets=None, rules=None):
        self.default_target = default_target
        self.targets = targets
        self.rules = rules

    def __str__(self):
        return "Config(default-target: %s)" % self.default_target


class TargetSpec:
    def __init__(self, spec):
        self.name = next(iter(spec))
        self.target = Target(spec[self.name])


class Target:
    def __init__(self, props):
        self.browser = props['browser']
        self.profile = props['profile']

    def __str__(self):
        return "Target(browser: {}, profile: {})"\
            .format(self.browser, self.profile)


class Rule:
    def __init__(self, props):
        self.url_pattern = props['url_pattern']
        self.pattern_type = props.get('pattern_type', 'ant')
        self.target = Target(props['target'])

    def __str__(self):
        return "Rule(url_pattern: {}, pattern_type: {}, target: {})"\
            .format(self.url_pattern, self.pattern_type, self.target)

