import proxlist


def test_random_proxy():
    random_proxy = proxlist.random_proxy()

    assert random_proxy in proxlist.proxies.PROXY_LIST


def test_list_proxies():
    proxy_list = proxlist.list_proxies()

    assert proxy_list == proxlist.proxies.PROXY_LIST

    
def test_proxy_dict():
    proxy_dict = proxlist.proxy_dict()
    http = proxy_dict.get('http', None)
    https = proxy_dict.get('https', None)


    assert proxy_dict is not None
    assert http is not None
    assert http.startswith('http://')
    assert https is not None
    assert https.startswith('https://')
