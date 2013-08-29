# timings.py

timings.py caluclates the average request times for a set of urls, broken down to **dns lookup** time, **tcp connection** time, **ssl handshake** time, **processing** time and **transfer** time.

## Installation

```bash
git clone git@github.com:kajic/url-timings.git
cd url-timings
pip install -r requirements.txt
```

## Usage

Given example-urls.txt with the following urls:

```
https://google.com
https://twitter.com
https://tumblr.com
https://facebook.com
https://wordpress.com
```

Running `python timings.py --urls example-urls.txt -c 20 --parallel` will produce the average times based on 20 requests for each url:

```bash
$ python timings.py --urls example-urls.txt -c 20 --parallel
....................................................................................................
+-----------------------+---------+-----------+-----------+---------+---------+---------+
| url                   |     dns |   tcp_con |   ssl_con |    calc |   trans |   total |
+=======================+=========+===========+===========+=========+=========+=========+
| https://google.com    | 0.03335 |   0.0332  |   0.96615 | 0.11625 | 0       | 1.14895 |
+-----------------------+---------+-----------+-----------+---------+---------+---------+
| https://twitter.com   | 0.027   |   0.1321  |   0.5013  | 0.15315 | 0.31865 | 1.1323  |
+-----------------------+---------+-----------+-----------+---------+---------+---------+
| https://tumblr.com    | 0.0216  |   0.11405 |   0.56505 | 0.1032  | 0.0001  | 0.8043  |
+-----------------------+---------+-----------+-----------+---------+---------+---------+
| https://facebook.com  | 0.22535 |   0.1307  |   0.46645 | 0.20455 | 0       | 1.0271  |
+-----------------------+---------+-----------+-----------+---------+---------+---------+
| https://wordpress.com | 0.07755 |   0.1748  |   0.57915 | 0.1912  | 0.02625 | 1.04895 |
+-----------------------+---------+-----------+-----------+---------+---------+---------+
```

timings.py uses [curl](http://curl.haxx.se/) to make requests and generate timings. The following description of table columns is an adaptation of curl's [`--write-out` option](http://curl.haxx.se/docs/manpage.html).

* `dns` - The time, in seconds, it took for name resolving to complete.
* `tcp_con` - The time, in seconds, it took for the TCP connection to the remote host (or proxy) to be established.
* `ssl_con` - The time, in seconds, it took for the SSL/SSH/etc connect/handshake to the remote host to be completed.
* `calc` - The time, in seconds, it took for the server to process the request.
* `trans` - The time, in seconds, it took for the response to be transfered.
* `total` - The total time for the request, in seconds.


### Options
```doc
Usage:
  timings.py [--urls=URLS] [--fetch-count=COUNT] [--parallel]
  timings.py --version

Options:
  -h --help               show this help message and exit
  -v --version            show version and exit
  -u --urls=URLS          path to urls file (one url per line)
  -c --fetch-count=COUNT  number of times to fetch each url [default: 5]
  -p --parallel           do requests in parallel
"""
```
