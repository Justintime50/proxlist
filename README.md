<div align="center">

# Proxlist

Retrieve proxy servers.

[![Build Status](https://github.com/Justintime50/proxlist/workflows/build/badge.svg)](https://github.com/Justintime50/proxlist/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/proxlist/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/proxlist?branch=main)
[![PyPi](https://img.shields.io/pypi/v/proxlist)](https://pypi.org/project/proxlist)
[![Licence](https://img.shields.io/github/license/Justintime50/proxlist)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/proxlist/showcase.png" alt="Showcase">

</div>

Finding and storing a list of proxies can be taxing - especially ones that are free and may not work only minutes from now. `proxlist` will validate the proxy and return a rotating random proxy to you so you don't need to keep a list of proxies or ensure it's contents are still valid.

Proxies are returned in the form of strings (eg: `ip:port`).

These proxies come from all over the world and may not be performant for a production application. This package (for now) is intended for testing purposes and I make no guarantee about where the data sent through these proxies goes or how it's handled. The list of proxies rotates rapidly and is free and open source.

## Install

```bash
# Install tool
pip3 install proxlist

# Install locally
make install
```

## Usage

```python
import proxlist
import requests

proxy = proxlist.random_proxy()

# You can also filter proxies by country or google_verified
# proxies = proxlist.random_proxy(country='US', google_verified=True)

# Alternatively, you could get the entire list of current proxies (and could optionally filter them like above)
# proxies = proxlist.list_proxies()

proxies = {
    'http': f'http://{proxy}',
    'https': f'http://{proxy}',
}

# Depending on the proxy and you location in the world, you may need to adjust the timeout
# to provide the proxy enough time to route your request.
response = requests.get('https://google.com', proxies=proxies, timeout=10)
print(response.text)
```

## Development

```bash
# Get a comprehensive list of development tools
make help
```
