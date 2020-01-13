import yaml


def config_constructor(loader, node):
    objects = loader.construct_mapping(node, deep=True)
    rules = map(Rule, objects['rules'])
    targets = map(Target, objects['targets'])
    return Config(Target(objects['default_target']), targets, rules)


class Config(yaml.YAMLObject):
    yaml_tag = '!Config'

    def __init__(self, default_target=None, targets=None, rules=None):
        self.default_target = default_target
        self.targets = targets
        self.rules = rules

    def __str__(self):
        return "Config(default-target: %s)" % self.default_target


class Target:
    def __init__(self, props):
        self.browser = props['browser']
        self.profile = props.get('profile', 'Default')
        self.incognito = props.get('incognito', False)

    def __str__(self):
        return '{}\n{}\n{}'.format(self.browser, self.profile, self.incognito)


class Rule:
    def __init__(self, props):
        self.url_pattern = props['url_pattern']
        self.pattern_type = props.get('pattern_type', 'ant')
        self.target = Target(props['target'])

    def __str__(self):
        return "Rule(url_pattern: {}, pattern_type: {}, target: {})"\
            .format(self.url_pattern, self.pattern_type, self.target)

