# CHANGELOG

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
