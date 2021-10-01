import pytest

from services.favicon_grabber_service import FavIconGrabber


class TestFavIconGrabber:
    json_response = {"domain": "github.com",
                     "icons": [{"src": "https://github.githubassets.com/favicons/favicon.svg", "type": "image/svg+xml"},
                               {"src": "https://github.githubassets.com/pinned-octocat.svg"},
                               {"src": "https://github.com/fluidicon.png"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-114x114.png",
                                "sizes": "114x114"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-120x120.png",
                                "sizes": "120x120"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-144x144.png",
                                "sizes": "144x144"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-152x152.png",
                                "sizes": "152x152"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-180x180.png",
                                "sizes": "180x180"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-57x57.png", "sizes": "57x57"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-60x60.png", "sizes": "60x60"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-72x72.png", "sizes": "72x72"},
                               {"src": "https://github.githubassets.com/apple-touch-icon-76x76.png", "sizes": "76x76"},
                               {"src": "https://github.githubassets.com/app-icon-192.png", "sizes": "192x192",
                                "type": "image/png"},
                               {"src": "https://github.githubassets.com/app-icon-512.png", "sizes": "512x512",
                                "type": "image/png"},
                               {"src": "https://github.com/favicon.ico", "type": "image/x-icon"}]}

    @pytest.fixture
    def icon_grabber_fixture(self):
        url = 'https://github.com/'
        return FavIconGrabber(url)

    @pytest.fixture
    def get_icons_from_api_fixture(self, requests_mock, icon_grabber_fixture):
        requests_mock.get(icon_grabber_fixture.call_url, json=self.json_response)

    def test_get_icons_from_api(self, requests_mock, icon_grabber_fixture):
        requests_mock.get(icon_grabber_fixture.call_url, json=self.json_response)

        result = icon_grabber_fixture.get_icons_from_api()

        assert result

    def test_get_icons_from_api_when_404(self, requests_mock, icon_grabber_fixture):
        requests_mock.get(icon_grabber_fixture.call_url, status_code=404)

        result = icon_grabber_fixture.get_icons_from_api()

        assert len(result) == 0

    def test_get_icon(self, icon_grabber_fixture, get_icons_from_api_fixture):
        result = icon_grabber_fixture.get_icon(min_icon_size=0)
        assert 'http' in result

    def test_get_size_number(self, icon_grabber_fixture):
        result = icon_grabber_fixture.get_size_number('180x180')
        assert result == 180

    def test_get_size_number_when_input_is_wrong(self, icon_grabber_fixture):
        result = icon_grabber_fixture.get_size_number('wrong_input')
        assert result == 0