import requests
from django.conf import settings
from requests import ConnectionError, Timeout

from services.common import get_base_url


class FavIconGrabber:
    def __init__(self, url: str):
        self.url = url
        self.base_url = get_base_url(self.url)
        self.api_url = settings.FAVICON_GRABBER_URL
        self.call_url = self.api_url + self.base_url

    @staticmethod
    def get_size_number(size: str) -> int:
        try:
            return int(size.split('x')[0])
        except (IndexError, ValueError):
            return 0

    def get_icon(self, min_icon_size: int) -> str:
        for item in self.get_icons_from_api():
            if 'sizes' in item:
                if self.get_size_number(item.get('sizes')) >= min_icon_size:
                    return item.get('src')
            else:
                return item.get('src')

    def get_icons_from_api(self) -> list:
        try:
            r = requests.get(self.call_url)
            if r.status_code == 200:
                return r.json().get('icons')
            return []
        except (ConnectionError, Timeout):
            return []