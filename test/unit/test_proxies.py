import proxlist


def test_random_proxy():
    proxy_list = proxlist.proxies._open_proxy_list()
    random_proxy = proxlist.random_proxy()

    assert random_proxy in proxy_list


def test_list_proxies():
    proxy_list = proxlist.proxies._open_proxy_list()
    retrieved_proxy_list = proxlist.list_proxies()

    assert retrieved_proxy_list == proxy_list


def test_open_proxy_list():
    proxy_list = proxlist.proxies._open_proxy_list()

    assert type(proxy_list) == list
    assert len(proxy_list) > 10
