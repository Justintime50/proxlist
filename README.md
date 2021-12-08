<div align="center">

# Proxlist

Retrieve proxy servers.

[![Build Status](https://github.com/Justintime50/proxlist/workflows/build/badge.svg)](https://github.com/Justintime50/proxlist/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/proxlist/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/proxlist?branch=main)
[![PyPi](https://img.shields.io/pypi/v/proxlist)](https://pypi.org/project/proxlist)
[![Licence](https://img.shields.io/github/license/Justintime50/proxlist)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/proxlist/showcase.png" alt="Showcase">

</div>

Finding and storing a list of proxies can be taxing. Simply import `proxlist` and have it give you a rotating random proxy to run your requests through.

The list of currently configured proxies have `SSL` support, were tested to be able to accept connections (3 independant tests to ensure consistency), and were able to serve requests within 15 seconds (your mileage may vary based on the content you are sending/receiving through the proxy and where you are located in the world, if you receive timeouts, simply bump the timeout up or try again). This may change over time as proxies change and the list gets updated.

Proxies are returned in the form of strings (eg: `ip:port`).

These proxies come from all over the world and may not be performant, this package is intended for testing purposes and I make no guarantee about where the data sent through these proxies goes - this package should not (yet) be considered for production applications.

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

# Alternatively, you could get the entire list of configured proxies
# proxies = proxlist.list_proxies()

proxies = {
    'http': f'http://{proxy}',
    'https': f'http://{proxy}',
}

response = requests.get('https://google.com', proxies=proxies)
print(response.text)
```

## Development

```bash
# Get a comprehensive list of development tools
make help
```
