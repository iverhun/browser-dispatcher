
class Chrome:
    def __init__(self, target=None, url=None):
        self.target = target
        self.url = url

    def command(self):
        return (self._open_incognito if self.target.incognito else self._open_in_profile)()

    def _open_in_profile(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="{}" "{}" >> /dev/null &' \
            .format(self.target.profile, self.url)

    def _open_incognito(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="{}" --incognito "{}" >> /dev/null &'\
            .format(self.target.profile, self.url)
