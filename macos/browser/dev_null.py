

class DevNull:
    def __init__(self, target=None, url=None):
        self.target = target
        self.url = url

    def command(self):
        return 'echo "Url %s was not opened" >> /dev/null &' % self.url
