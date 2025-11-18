from concurrent.futures import (
    ALL_COMPLETED,
    ThreadPoolExecutor,
    wait,
)
from typing import (
    List,
    Optional,
)

import requests
import woodchips
from bs4 import BeautifulSoup  # type: ignore


LOGGER_NAME = "proxlist"
NUM_THREADS = 20
LOG_LEVEL = "NOTSET"  # Intentionally hide all loggers. During development, set to `DEBUG`


def random_proxy(country: Optional[str] = None, google_verified: bool = False) -> Optional[str]:
    """Returns a 'random' proxy (ip:port) from the currently configured list.

    This is accomplished by testing each proxy concurrently until we find one that works.
    """
    _setup_logger()
    logger = woodchips.get(LOGGER_NAME)

    validate_proxy_timeout = 2 if country or google_verified else 1

    proxy_list = get_proxies(country, google_verified)
    logger.debug(proxy_list)

    thread_list = []
    pool = ThreadPoolExecutor(NUM_THREADS)

    for proxy in proxy_list:
        proxy_thread = pool.submit(
            validate_proxy,
            proxy=proxy,
            timeout=validate_proxy_timeout,
        )
        thread_list.append(proxy_thread)

    wait(thread_list, return_when=ALL_COMPLETED)
    valid_proxy_list = [proxy.result() for proxy in thread_list if proxy.result()]

    if valid_proxy_list:
        return valid_proxy_list[0]
    else:
        raise Exception("No working proxies were found at this time, please try again later.")


def list_proxies(country: Optional[str] = None, google_verified: bool = False) -> List[str]:
    """Lists all proxies from the currently configured list."""
    proxy_list = get_proxies(country, google_verified)

    return proxy_list


def get_proxies(country: Optional[str] = None, google_verified: bool = False) -> List[str]:
    """Gets a list of proxies from https://www.sslproxies.org by scraping the proxy table."""
    proxy_list = []

    website = requests.get(
        url="https://www.sslproxies.org",
        timeout=3,
    )

    soup = BeautifulSoup(website.text, "html.parser")
    tbody = None
    if soup:
        table = soup.find("table")
        if table:
            tbody = table.find("tbody")

    if tbody is None:
        raise Exception("Could not find proxy table content!")

    for table_entry in tbody.find_all("tr"):  # type:ignore
        entry_elements = [td.text.strip() for td in table_entry.find_all("td")]
        ip_address = entry_elements[0]
        port = entry_elements[1]
        country_code = entry_elements[2]  # Two digit ISO country code
        is_google_verified = True if entry_elements[5] == "yes" else False

        proxy = f"{ip_address}:{port}"

        # If the user specified filters, respect them here
        if (country is not None and country_code == country) and (
            google_verified and is_google_verified
        ):  # pragma: no cover - cannot reliably get country + google-verified filtered results
            proxy_list.append(proxy)
        elif (country is not None and country_code == country) and (not google_verified):
            proxy_list.append(proxy)
        elif (country is None) and (google_verified and is_google_verified):
            proxy_list.append(proxy)
        elif (country is None) and (google_verified is False):
            proxy_list.append(proxy)

    if len(proxy_list) == 0:
        raise ValueError("There are no proxies with your specified criteria at this time. Please try again later.")

    return proxy_list


def validate_proxy(proxy: str, timeout: float) -> Optional[str]:
    """Validates that a proxy is working (these free proxies can come and go within minutes),
    test them before returning to the user.
    """
    logger = woodchips.get(LOGGER_NAME)

    url = "https://google.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    }
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }

    try:
        with requests.get(url, proxies=proxies, headers=headers, timeout=timeout, stream=True) as response:
            if response.raw.connection and response.raw.connection.sock:
                if response.raw.connection.sock.getpeername()[0] == proxies["http"].split(":")[1][2:]:
                    valid_proxy = proxy
                    logger.debug(f"Found valid proxy: {proxy}")
    except Exception:
        # Couldn't connect to proxy, discard
        valid_proxy = None
        logger.debug(f"Couldn't connect to proxy: {proxy}")

    return valid_proxy


def _setup_logger():
    """Setup a `woodchips` logger instance."""
    logging_level = LOG_LEVEL

    logger = woodchips.Logger(
        name=LOGGER_NAME,
        level=logging_level,
    )
    logger.log_to_console()


if __name__ == "__main__":
    print(random_proxy())
