from services.site_info import get_base_url


class TestCommonFunctions:
    def test_get_base_url(self):
        url = 'https://daemon.codes'
        expected_url = 'daemon.codes'
        result = get_base_url(url)
        assert result == expected_url

    def test_get_base_url_with_wrong_url(self):
        url = 'some_wrong_url'
        result = get_base_url(url)
        assert result is None
