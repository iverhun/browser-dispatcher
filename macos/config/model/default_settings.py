from .target import Target


class DefaultSettings:
    def __init__(self, props):
        self.target = Target(props['target'])
        self.ignore_url_schema = props.get('ignore_url_schema', True)

    def __str__(self):
        return "Defaults(target: %s, ignore_url_schema: %s)" % (self.target, self.ignore_url_schema)
