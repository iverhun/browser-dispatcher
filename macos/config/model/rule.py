from .target import Target


class Rule:
    def __init__(self, props):
        self.url_pattern = props['url_pattern']
        self.pattern_type = props.get('pattern_type', 'ant')
        self.target = Target(props['target'])

    def __str__(self):
        return "Rule(url_pattern: {}, pattern_type: {}, target: {})"\
            .format(self.url_pattern, self.pattern_type, self.target)
