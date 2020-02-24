from .chrome import Chrome
from .dev_null import DevNull


class Browsers:
    def __init__(self):
        pass

    @staticmethod
    def chrome(target, url):
        return Chrome(target, url)

    @staticmethod
    def devnull(target, url):
        return DevNull(target, url)


def browser(target, url):
    try:
        return getattr(Browsers, target.browser)(target, url)
    except AttributeError as e:
        raise Exception('Unsupported Browser: {}'.format(target.browser)) from e
