import urllib.request
from dataclasses import dataclass
from urllib.error import URLError

from bs4 import BeautifulSoup
from rest_framework.exceptions import NotFound

from services.common import get_base_url


@dataclass
class SiteInfoResponse:
    title: str
    description: str
    base_url: str


class SiteInfoService:
    def __init__(self, url: str):
        self.url = url
        self.page = self.get_page()

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