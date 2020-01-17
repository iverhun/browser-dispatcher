_chrome_executable = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
_chrome_profiles_dir = '$HOME/Library/Application\ Support/Google/Chrome/'


class Chrome:

    def __init__(self, target=None, url=None):
        self.target = target
        self.url = url

    def command(self):
        return (self._open_incognito if self.target.incognito else self._open_in_profile)()

    @staticmethod
    def list_profiles_command():
        return """
            find {}/* -name Preferences -print0 | xargs -I % -0 jq -r  "[{name: .profile.name, file:\"%\"}] | map_values({name: .name, profile: .file | split(\"/\")[-2] })" %
            """.format(_chrome_profiles_dir)

    def _open_in_profile(self):
        return '{} --profile-directory="{}" "{}" >> /dev/null &' \
            .format(_chrome_executable, self.target.profile, self.url)

    def _open_incognito(self):
        return '{} --profile-directory="{}" --incognito "{}" >> /dev/null &' \
            .format(_chrome_executable, self.target.profile, self.url)
