from unittest.mock import patch

import pytest

import proxlist


def test_random_proxy():
    """Tests that we can retrieve a random proxy.

    TODO: This test is flakey and relies on a valid proxy getting returned and connecting
    which may not always happen. Find a way to ensure consistent test results.
    """
    random_proxy = proxlist.random_proxy()

    assert type(random_proxy) == str
    assert 12 < len(random_proxy) < 25


def test_random_proxy_filter_country():
    """Tests that we can retrieve a random proxy when filtering by country."""
    countries_to_try = ['US', 'CA', 'MX']

    for country in countries_to_try:
        try:
            random_proxy = proxlist.random_proxy(country=country)
        except Exception:
            # If we fail to find a valid proxy from one country, try another country
            # This is a hack to make this test less flakey on transient failures
            continue

        assert type(random_proxy) == str
        assert 12 < len(random_proxy) < 25


def test_random_proxy_filter_google_verified():
    """Tests that we can retrieve a random proxy when filtering for a google verified proxy.

    TODO: This test is flakey and relies on a valid proxy getting returned and connecting
    which may not always happen. Find a way to ensure consistent test results.
    """
    random_proxy = proxlist.random_proxy(google_verified=True)

    assert type(random_proxy) == str
    assert 12 < len(random_proxy) < 25


@patch('proxlist.proxies._validate_proxy')
def test_random_proxy_no_valid_proxies(mock_validate_proxy):
    """Tests that we raise an error when no proxies are found."""
    message = 'No working proxies were found at this time, please try again later.'
    with pytest.raises(Exception) as error:
        _ = proxlist.random_proxy()

        assert message == str(error.value)


def test_get_proxies_no_proxies_based_on_criteria():
    """Tests that we raise an error when no proxies are found based on the criteria specified."""
    message = 'There are no proxies with your specified criteria at this time. Please try again later.'
    with pytest.raises(ValueError) as error:
        _ = proxlist.proxies._get_proxies('BAD_COUNTRY')

        assert message == str(error.value)


def test_list_proxies():
    """Tests that we can retrieve a list of proxies from the free proxy website."""
    proxy_list = proxlist.list_proxies()

    assert type(proxy_list) == list
    assert len(proxy_list) > 10
