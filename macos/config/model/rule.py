from .target import Target


class Rule:
    def __init__(self, props, defaults):
        self.target = Target(props['target'])
        self.ignore_url_schema = props.get('ignore_url_schema', defaults.ignore_url_schema)

    def apply(self, url, matcher):
        pass


class UrlRule(Rule):
    def __init__(self, props, defaults):
        Rule.__init__(self, props, defaults)
        self.url_pattern = props['url_pattern']
        self.pattern_type = props.get('pattern_type', 'ant')

    def __str__(self):
        return "Rule(url_pattern: {}, pattern_type: {}, target: {})"\
            .format(self.url_pattern, self.pattern_type, self.target)

    def apply(self, url, matcher):
        return matcher(url, self.url_pattern)


class HostsRule(Rule):
    def __init__(self, props, defaults):
        Rule.__init__(self, props, defaults)
        self.hosts = props.get('hosts', None)
        self.pattern_type = 'hosts'

    def __str__(self):
        return "HostRule(hosts: {}, target: {})"\
            .format(self.hosts, self.target)

    def apply(self, url, matcher):
        return matcher(url, self.hosts)
