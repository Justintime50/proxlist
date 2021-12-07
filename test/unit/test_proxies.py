import proxlist


def test_random_proxy():
    random_proxy = proxlist.random_proxy()

    assert random_proxy in proxlist.proxies.PROXY_LIST


def test_list_proxies():
    proxy_list = proxlist.list_proxies()

    assert proxy_list == proxlist.proxies.PROXY_LIST
