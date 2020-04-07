

class Safari:
    def __init__(self, target=None, url=None):
        self.target = target
        self.url = url

    def command(self):
        return 'open -a Safari %s >> /dev/null &' % self.url
