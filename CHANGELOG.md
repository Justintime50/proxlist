# CHANGELOG

## v1.1.0 (2024-10-10)

- Adds error handling when BeautifulSoup cannot find the table of proxies
- Python 3.13 compatibility

## v1.0.1 (2024-04-11)

- Adds Python 3.12 support
- Bumps woodchips to v1 to match supported python versions for this package

## v1.0.0 (2023-07-01)

- Drops support for Python 3.7

## v0.5.1 (2023-04-12)

- Adds a missing timeout to retrieving the list of proxies

## v0.5.0 (2022-03-04)

- Adds concurrency to speed up validating proxies. This brings finding a valid proxy from `~1.5 minutes` down to just `~4-20 seconds` depending on the available proxies at the time
- Bumps thread count from `10` to `20`
- Bumps timeout to validate a proxy from `0.5` to `1` second with no filters and `3` to `2` seconds with filters
- Exposes `list_proxies` and `validate_proxy` functions which were previously internal
- Adds timers to test results and brings coverage to 100%

## v0.4.0 (2022-02-10)

- Adds debug logging
- Fixes a bug that would choose an incorrect random proxy after finding a verified entry, this fix greatly increases the reliability of this package
- Other small improvements to increase performance

## v0.3.0 (2021-12-08)

- Adds `country` parameter to filter proxies by their two digit ISO country codes
- Adds `google_verified` parameter to filter proxies by if they are google verified or not
- Adds altered timeout logic (shorter timeouts for larger proxy pools to get to a working proxy faster, longer timeouts when the proxy pool is smaller to offset the difference and get a working proxy back to you)

## v0.2.1 (2021-12-08)

- Have a stricter validation timeout of 1 second instead of 3 seconds to improve performance and accuracy based on your connection and location

## v0.2.0 (2021-12-07)

- Removes proxy list from repo entirely
- Retrieves an updated proxy list each time you request a proxy
- Tests that the proxy works prior to returning it to you

## v0.1.1 (2021-12-07)

- Overhauls the proxy list with different proxies (tested more thoroughly) as well as moves the list from a hardcoded constant to a text file

## v0.1.0 (2021-12-06)

- Initial release allowing you to retrieve a random proxy or a list of proxies from a small initial list
