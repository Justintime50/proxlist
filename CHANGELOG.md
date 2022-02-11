# CHANGELOG

## v0.4.0 (2022-02-10)

* Adds debug logging
* Fixes a bug that would choose an incorrect random proxy after finding a verified entry, this fix greatly increases the reliability of this package
* Other small improvements to increase performance

## v0.3.0 (2021-12-08)

* Adds `country` parameter to filter proxies by their two digit ISO country codes
* Adds `google_verified` parameter to filter proxies by if they are google verified or not
* Adds altered timeout logic (shorter timeouts for larger proxy pools to get to a working proxy faster, longer timeouts when the proxy pool is smaller to offset the difference and get a working proxy back to you)

## v0.2.1 (2021-12-08)

* Have a stricter validation timeout of 1 second instead of 3 seconds to improve performance and accuracy based on your connection and location

## v0.2.0 (2021-12-07)

* Removes proxy list from repo entirely
* Retrieves an updated proxy list each time you request a proxy
* Tests that the proxy works prior to returning it to you

## v0.1.1 (2021-12-07)

* Overhauls the proxy list with different proxies (tested more thoroughly) as well as moves the list from a hardcoded constant to a text file

## v0.1.0 (2021-12-06)

* Initial release allowing you to retrieve a random proxy or a list of proxies from a small initial list
