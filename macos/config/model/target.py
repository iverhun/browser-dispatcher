class Target:
    def __init__(self, props):
        self.browser = props['browser'].lower()
        self.profile = props.get('profile', 'Default')
        self.incognito = props.get('incognito', False)

    def __str__(self):
        return '{}\n{}\n{}'.format(self.browser, self.profile, self.incognito)
