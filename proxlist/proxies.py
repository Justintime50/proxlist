import random
from typing import List

# The following proxy list was generated from https://www.sslproxies.org/ by ensuring:
# 1. Each proxy could handle connections
# 2. Each proxy had SSL (HTTPS) support
# 3. Each proxy could service requests in under 10 seconds
# NOTE: The items above may change without notice for each proxy as could the integrity of this list.
# TODO: Make this configurable as a JSON file and allow users to import a custom list of proxies
PROXY_LIST = [
    "103.124.2.229:3128",
    "18.183.102.198:8899",
    "181.10.230.100:57148",
    "181.52.85.249:36107",
    "197.248.184.157:53281",
    "200.69.79.220:55443",
    "203.193.131.74:3128",
    "221.139.11.208:8080",
    "8.210.219.124:59394",
    "85.195.104.71:80",
    "89.189.181.161:55855",
]


def random_proxy() -> str:
    random_proxy = random.choice(PROXY_LIST)

    return random_proxy


def list_proxies() -> List[str]:
    return PROXY_LIST
