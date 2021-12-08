import random
from typing import List

import requests
from bs4 import BeautifulSoup  # type: ignore


def random_proxy() -> str:
    """Returns a random proxy (ip:port) from the currently configured list."""
    valid_proxy_exists = False
    proxy_list = _get_proxies()

    for proxy in proxy_list:
        if _validate_proxy(proxy):
            valid_proxy_exists = True
            random_proxy = random.choice(proxy_list)
            break

    if valid_proxy_exists is False:
        raise Exception('No working proxies were found at this time, please try again later.')

    return random_proxy


def list_proxies() -> List[str]:
    """Lists all proxies from the currently configured list."""
    proxy_list = _get_proxies()

    return proxy_list


def _get_proxies() -> List[str]:
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
        # TODO: Eventually get more info like the country, anonymity, etc from this list

        proxy = f'{ip_address}:{port}'
        proxy_list.append(proxy)

    return proxy_list


def _validate_proxy(proxy: str) -> bool:
    """Validates that a proxy is working (these free proxies can come and go within minutes),
    test them before returning to the user.
    """
    proxy_works = False

    url = 'https://google.com'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    }
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }

    try:
        # A `3` second timeout here is pretty generous, but it's what we are going with for now
        with requests.get(url, proxies=proxies, headers=headers, timeout=3, stream=True) as r:
            if r.raw.connection.sock:
                if r.raw.connection.sock.getpeername()[0] == proxies['http'].split(':')[1][2:]:
                    proxy_works = True
    except Exception:
        # Couldn't connect to proxy, discard
        pass

    return proxy_works
