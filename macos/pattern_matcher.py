import re
import fnmatch


class PatternMatcher:
    def __init__(self):
        pass

    @staticmethod
    def ant(url, pattern):
        return fnmatch.fnmatch(url, pattern)

    @staticmethod
    def regex(url, pattern):
        return re.match(pattern, url) is not None
