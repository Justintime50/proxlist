from unittest.mock import patch

import pytest
import requests

import proxlist


def test_random_proxy():
    """Tests that we can retrieve a random proxy."""
    for _ in range(3):
        try:
            random_proxy = proxlist.random_proxy()
        except Exception:
            # If we fail to find a valid proxy, try again a couple more times before failing
            continue

        assert isinstance(random_proxy, str)
        assert ":" in random_proxy
        assert 12 < len(random_proxy) < 25


def test_random_proxy_filter_country():
    """Tests that we can retrieve a random proxy when filtering by country."""
    countries_to_try = [
        "US",
        "CA",
        "MX",
    ]  # Purposefully sorted by distance from most-likely origin so tests run faster

    for country in countries_to_try:
        try:
            random_proxy = proxlist.random_proxy(country=country)
        except Exception:
            # If we fail to find a valid proxy from one country, try another country
            continue

        assert isinstance(random_proxy, str)
        assert ":" in random_proxy
        assert 12 < len(random_proxy) < 25


def test_random_proxy_filter_google_verified():
    """Tests that we can retrieve a random proxy when filtering for a google verified proxy."""
    for _ in range(3):
        try:
            random_proxy = proxlist.random_proxy(google_verified=True)
        except Exception:
            # If we fail to find a valid proxy, try again a couple more times before failing
            continue

        assert isinstance(random_proxy, str)
        assert ":" in random_proxy
        assert 12 < len(random_proxy) < 25


@patch("proxlist.proxies.get_proxies", return_value=[])
def test_random_proxy_no_proxies_list(mock_get_proxies):
    """Tests that we raise an error when no proxies are found."""
    message = "No working proxies were found at this time, please try again later."
    with pytest.raises(Exception) as error:
        _ = proxlist.random_proxy()

    assert str(error.value) == message


@patch("proxlist.proxies.get_proxies", return_value=[])
@patch("proxlist.proxies.validate_proxy", return_value=None)
def test_random_proxy_no_valid_proxies(mock_validate_proxy, mock_get_proxies):
    """Tests that we raise an error when there are no valid proxies."""
    message = "No working proxies were found at this time, please try again later."
    with pytest.raises(Exception) as error:
        _ = proxlist.random_proxy()

    assert str(error.value) == message


def test_get_proxies_no_proxies_based_on_criteria():
    """Tests that we raise an error when no proxies are found based on the criteria specified."""
    message = "There are no proxies with your specified criteria at this time. Please try again later."
    with pytest.raises(ValueError) as error:
        _ = proxlist.get_proxies("BAD_COUNTRY")

    assert str(error.value) == message


@patch("requests.get", side_effect=requests.exceptions.RequestException("mock-error"))
def test_get_proxies_requests_error(mock_requests_error):
    """Tests we re-raise an exception when we fail to get the proxy list."""
    with pytest.raises(requests.exceptions.RequestException) as error:
        _ = proxlist.get_proxies(None)

    assert str(error.value) == "mock-error"


def test_list_proxies():
    """Tests that we can retrieve a list of proxies from the free proxy website."""
    proxy_list = proxlist.list_proxies()

    assert isinstance(proxy_list, list)
    assert len(proxy_list) > 50  # The list should typically be ~100 records


@patch("woodchips.Logger")
def test_setup_logger(mock_logger):
    proxlist.proxies._setup_logger()

    mock_logger.assert_called_once()
