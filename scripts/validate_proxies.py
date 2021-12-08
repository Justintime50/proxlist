import os
from threading import Thread
from typing import List, Optional

import requests

# This script can be used to test the validity of a list of proxies

# The following rules are the criteria for a proxy to make it into the library:
# 1. Each proxy can handle at least 3 separate connections (proves consistency)
# 2. Each proxy has SSL (HTTPS) support
# 3. Each proxy could service requests in under 15 seconds (performant, 15 seconds chosen for "around the world" buffer)
# NOTE: The items above may change without notice for each proxy as could the integrity of this list.


def main():
    """Print to console the proxies that pass the test.

    If proxies appear in the list the number of times of the range below, they are consistently working.
    You can then discard any that didn't appear X number of times.
    """
    proxy_list = proxies_to_validate()
    for proxy in proxy_list:
        for i in range(3):
            Thread(
                target=test_proxy,
                args=(proxy,),
            ).start()


def proxies_to_validate() -> List[str]:
    """Return a list of proxies to validate from a text file.

    These can be procured from a website such as: https://www.sslproxies.org/
    """
    proxy_filepath = os.path.join('data', 'proxies_to_validate.txt')
    with open(proxy_filepath, 'r') as filename:
        data = filename.readlines()
        proxy_list = [line_item.replace('\n', '').strip() for line_item in data]

    return proxy_list


def test_proxy(proxy: str) -> Optional[str]:
    """We test the proxy works by sending a request to this endpoint
    which returns the current IP address, if we connect, we'll get the new
    IP address of the proxy.
    """
    url = "http://api.ipify.org"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Accept-Language": "en-US,en;q=0.5",
    }
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }

    try:
        response = requests.get(url, proxies=proxies, headers=headers, timeout=15)
        # Only include proxies that are an actual proxy
        if response.text is not None and len(response.text) < 25 and len(response.text) > 12:
            ip_with_port = (
                proxy.split(":")[0] + ":" + proxy.split(":")[1]
            )  # Some redirect the IP here so we grab the original
            print(ip_with_port)
        proxy_response = response.text
    except Exception:
        # Couldn't connect to proxy, discard
        proxy_response = None
        pass

    return proxy_response


if __name__ == "__main__":
    main()
