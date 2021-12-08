import random
from typing import List, Optional

import requests
from bs4 import BeautifulSoup  # type: ignore


def random_proxy(country: Optional[str] = None, google_verified: bool = False) -> str:
    """Returns a random proxy (ip:port) from the currently configured list."""
    valid_proxy_exists = False
    validate_proxy_timeout = 5 if country or google_verified else 1  # Set a longer timeout if our proxy pool is smaller
    proxy_list = _get_proxies(country, google_verified)

    for proxy in proxy_list:
        # TODO: In the future, we could maybe implement threading here to quickly validate every proxy
        # and break on the first success, we'll need to ensure we handle it properly.
        if _validate_proxy(proxy, validate_proxy_timeout):
            valid_proxy_exists = True
            random_proxy = random.choice(proxy_list)
            break

    if valid_proxy_exists is False:
        raise Exception('No working proxies were found at this time, please try again later.')

    return random_proxy


def list_proxies(country: Optional[str] = None, google_verified: bool = False) -> List[str]:
    """Lists all proxies from the currently configured list."""
    proxy_list = _get_proxies(country, google_verified)

    return proxy_list


def _get_proxies(country: Optional[str] = None, google_verified: bool = False) -> List[str]:
    """Gets a list of proxies from https://www.sslproxies.org by scraping the proxy table."""
    proxy_list = []

    try:
        website = requests.get('https://www.sslproxies.org')
    except Exception:
        raise

    soup = BeautifulSoup(website.text, 'html.parser')
    table = soup.find('table').find('tbody')

    for table_entry in table.find_all('tr'):
        entry_elements = [td.text.strip() for td in table_entry.find_all('td')]
        ip_address = entry_elements[0]
        port = entry_elements[1]
        country_code = entry_elements[2]  # Two digit ISO country code
        is_google_verified = True if entry_elements[5] == 'yes' else False

        proxy = f'{ip_address}:{port}'

        # If the user specified filters, respect them here
        if (country is not None and country_code == country) and (google_verified and is_google_verified):
            proxy_list.append(proxy)
        elif (country is not None and country_code == country) and (not google_verified):
            proxy_list.append(proxy)
        elif (country is None) and (google_verified and is_google_verified):
            proxy_list.append(proxy)
        elif (country is None) and (google_verified is False):
            proxy_list.append(proxy)

    if len(proxy_list) == 0:
        raise ValueError('There are no proxies with your specified criteria at this time. Please try again later.')

    return proxy_list


def _validate_proxy(proxy: str, timeout: int) -> bool:
    """Validates that a proxy is working (these free proxies can come and go within minutes),
    test them before returning to the user.
    """
    proxy_works = False

    url = 'https://google.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    }
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }

    try:
        with requests.get(url, proxies=proxies, headers=headers, timeout=timeout, stream=True) as response:
            if response.raw.connection.sock:
                if response.raw.connection.sock.getpeername()[0] == proxies['http'].split(':')[1][2:]:
                    proxy_works = True
    except Exception:
        # Couldn't connect to proxy, discard
        pass

    return proxy_works
