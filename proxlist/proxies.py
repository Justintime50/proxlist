import os
import random
from typing import List


def random_proxy() -> str:
    """Returns a random proxy (ip:port) from the currently configured list."""
    proxy_list = _open_proxy_list()
    random_proxy = random.choice(proxy_list)

    return random_proxy


def list_proxies() -> List[str]:
    """Lists all proxies from the currently configured list."""
    proxy_list = _open_proxy_list()

    return proxy_list


def _open_proxy_list():
    """Opens the current proxy list text file."""
    proxy_filepath = os.path.join('proxlist', 'data', 'proxy_list.txt')
    with open(proxy_filepath, 'r') as filename:
        data = filename.readlines()
        proxy_list = [line_item.replace('\n', '').strip() for line_item in data]

    return proxy_list
