import re
import fnmatch
from urllib.parse import urlparse


class PatternMatcher:
    def __init__(self):
        pass

    @staticmethod
    def ant(url, pattern):
        return fnmatch.fnmatch(url, pattern)

    @staticmethod
    def regex(url, pattern):
        return re.match(pattern, url) is not None

    @staticmethod
    def hosts(url, hosts):
        url_details = urlparse(url)
        hostname = url_details.hostname

        if hostname.startswith("www."):
            hostname = hostname[4:]

        if hostname in hosts:
            return True

        if url_details.port:
            if (hostname + ":" + str(url_details.port)) in hosts:
                return True

        return False
