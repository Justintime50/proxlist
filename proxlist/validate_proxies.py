from threading import Thread
from typing import Optional

import requests

# This script can be used to test the validity of a list of proxies

# Craft an initial proxy list (such as the simplified example below) from a site such as https://www.sslproxies.org/
PROXIES = [
    "210.14.104.230:8080",
    "129.226.113.45:59394",
    "181.49.100.190:8080",
    "103.214.202.105:8080",
]


def main():
    for proxy in PROXIES:
        Thread(
            target=test_proxy,
            args=(proxy,),
        ).start()


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
    proxy_reponse = None

    try:
        response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
        # Only include proxies that are an actual proxy
        if response.text is not None and len(response.text) < 25 and len(response.text) > 12:
            ip_with_port = (
                proxy.split(":")[0] + ":" + proxy.split(":")[1]
            )  # Some redirect the IP here so we grab the original
            print(ip_with_port)
    except Exception:
        # Couldn't connect to proxy, discard
        pass

    proxy_reponse = response.text

    return proxy_reponse


if __name__ == "__main__":
    main()
