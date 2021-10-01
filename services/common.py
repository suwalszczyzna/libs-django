import re


def get_base_url(url: str):
    match = re.search('http.?://([^/]+)', url)
    try:
        return match.group(1)
    except (IndexError, AttributeError):
        return None
