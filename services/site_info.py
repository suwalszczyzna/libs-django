import re
import urllib.request
from dataclasses import dataclass
from typing import Optional
from urllib.error import URLError

from bs4 import BeautifulSoup
import requests
from rest_framework.exceptions import NotFound


def get_base_url(url: str):
    match = re.search('http.?://([^/]+)', url)
    try:
        return match.group(1)
    except IndexError:
        return None


class FavIconGrabber:
    def __init__(self, url: str):
        self.url = url
        self.base_url = get_base_url(self.url)
        self.api_url = 'https://favicongrabber.com/api/grab/'

    @staticmethod
    def get_size_number(size: str) -> int:
        try:
            return int(size.split('x')[0])
        except IndexError:
            return 0

    def get_icon(self, min_icon_size: int):
        for item in self.get_icons_from_api():
            if 'sizes' in item:
                if self.get_size_number(item.get('sizes')) >= min_icon_size:
                    return item.get('src')
            else:
                return item.get('src')

    def get_icons_from_api(self) -> list:
        r = requests.get(self.api_url + self.base_url)
        print(r.status_code)
        if r.status_code == 200:
            return r.json().get('icons')
        else:
            raise NotFound(detail='Incorrect url')


@dataclass
class SiteInfoResponse:
    title: str
    description: str
    base_url: str


class SiteInfoService:
    def __init__(self, url: str):
        self.url = url
        self.page = self.get_page()
        self.favicon_grabber = FavIconGrabber(self.url)

    def get_page(self) -> BeautifulSoup:
        try:
            response = urllib.request.urlopen(self.url)
            return BeautifulSoup(response, 'html.parser', from_encoding=response.info().get_param('charset'))
        except URLError:
            raise NotFound(detail='Incorrect url')

    def get_description(self):
        if self.page.findAll("meta", attrs={"name": "description"}):
            return self.page.find("meta", attrs={"name": "description"}).get("content")

    def get_title(self):
        if self.page.findAll("title"):
            return self.page.find("title").string

    def get_meta_info(self) -> SiteInfoResponse:
        return SiteInfoResponse(
            title=self.get_title(),
            description=self.get_description(),
            base_url=get_base_url(self.url),
        )
