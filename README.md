<div align="center">

# Proxlist

Retrieve free, open-source proxy servers.

[![Build Status](https://github.com/Justintime50/proxlist/workflows/build/badge.svg)](https://github.com/Justintime50/proxlist/actions)
[![Coverage Status](https://img.shields.io/codecov/c/github/justintime50/proxlist)](https://app.codecov.io/github/Justintime50/proxlist)
[![PyPi](https://img.shields.io/pypi/v/proxlist)](https://pypi.org/project/proxlist)
[![Licence](https://img.shields.io/github/license/Justintime50/proxlist)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/proxlist/showcase.png" alt="Showcase">

</div>

Finding and storing a list of proxies can be taxing - especially ones that are free and actually work. `proxlist` will validate and return a rotating random proxy so you don't need to keep a list of proxies or ensure the list is still valid.

Proxies are returned in the form of strings (eg: `ip:port`).

These proxies come from all over the world and may not be performant for a production application. Instead, you should use a paid proxy service or a self-hosted solution. This package is intended for testing purposes and there are no guarantees about where the data sent through these proxies goes or how it's handled. The list and quality of proxies rotates rapidly - your mileage may vary.

## Install

```bash
# Install tool
pip3 install proxlist

# Install locally
just install
```

## Usage

```python
import proxlist
import requests

# Get a random proxy
proxy = proxlist.random_proxy()

# You can also filter proxies by country or google_verified
proxies = proxlist.random_proxy(country='US', google_verified=True)

# Alternatively, you could get the entire list of current proxies (and could optionally filter them like above)
proxies = proxlist.list_proxies()

# Depending on the proxy and your location in the world, you may need to adjust the timeout
# to provide the proxy enough time to route your request. Additionally, some of these proxies
# may be unstable - adding retry logic is highly recommended. Caching a working proxy is also
# a good idea with a fallback of retrying if the cached proxy no longer works or times out.
response = requests.get(
    'https://google.com',
    proxies={
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    },
    timeout=10,
)

print(response.text)
```

## Development

```bash
# Get a comprehensive list of development tools
just --list
```
