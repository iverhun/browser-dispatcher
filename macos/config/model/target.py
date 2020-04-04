class Target:
    def __init__(self, props):
        self.browser = props['browser'].lower()
        self.profile = props.get('profile', 'Default')
        self.incognito = props.get('incognito', False)
        self.incognito = props.get('app', False)
        self.guest = props.get('guest', False)

    def __str__(self):
        return '{}\n{}\n{}\n{}'.format(self.browser, self.profile, self.guest, self.incognito)
