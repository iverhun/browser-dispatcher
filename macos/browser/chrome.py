

class Chrome:
    def __init__(self, target=None, url=None):
        self.target = target
        self.url = url

    def command(self):
        if self.target.app:
            return self._open_app()
        if self.target.guest:
            return self._open_guest()
        if self.target.incognito:
            return self._open_incognito()
        return self._open_in_profile()

    def _open_in_profile(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="{}" "{}" >> /dev/null &' \
            .format(self.target.profile, self.url)

    def _open_app(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="{}" --app=git s"{}" >> /dev/null &'\
            .format(self.target.profile, self.url)

    def _open_guest(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --guest "{}" >> /dev/null &'\
            .format(self.url)

    def _open_incognito(self):
        return '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="{}" --incognito "{}" >> /dev/null &'\
            .format(self.target.profile, self.url)
