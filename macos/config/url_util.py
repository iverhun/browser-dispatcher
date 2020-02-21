import re


def normalize_url(url, strip_schema=True):
    pattern = re.compile(r"(https?://)?(www\.)?" if strip_schema else r"(www\.)?")
    return pattern.sub('', url).strip().strip('/')
