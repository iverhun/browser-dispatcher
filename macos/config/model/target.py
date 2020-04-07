class Target:
    def __init__(self, props):
        self.browser = props['browser'].lower()
        self.profile = props.get('profile', 'Default')
        self.incognito = props.get('incognito', False)
        self.incognito = props.get('app', False)
        self.guest = props.get('guest', False)

    def __str__(self):
        options = ""
        if self.guest:
            options = " (Guest)"
        if self.incognito:
            options = " (Incognito)"
        return '{} with {}{}'.format(self.browser.capitalize(), self.profile, options)
