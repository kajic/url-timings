# timings.py

timings.py records the average request times for a set of urls, broken down to **dns lookup** time, **tcp connection** time, **ssl handshake** time, **processing** time and **transfer** time. Upload and download sizes for all requests are also recorded.

## Requirements

Python and pip. 

## Installation

```bash
git clone git@github.com:kajic/url-timings.git
cd url-timings
pip install -r requirements.txt
```

## Usage

```bash
 python timings.py -u example-urls.txt
```

### Usage details

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
$ python timings.py -u example-urls.txt
.....
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
| url                   |   sizeu |   sized |   dns |   tcp_con |   ssl_con |   calc |   trans |   total |
+=======================+=========+=========+=======+===========+===========+========+=========+=========+
| https://google.com    |     141 |     572 | 0.027 |     0.038 |     0.118 |  0.076 |   0     |   0.259 |
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
| https://twitter.com   |     142 |   50704 | 0.049 |     0.137 |     0.302 |  0.216 |   0.404 |   1.108 |
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
| https://tumblr.com    |     141 |     163 | 0.06  |     0.118 |     0.273 |  0.12  |   0     |   0.571 |
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
| https://facebook.com  |     143 |     249 | 0.365 |     0.133 |     0.295 |  0.241 |   0     |   1.034 |
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
| https://wordpress.com |     144 |    8963 | 0.359 |     0.129 |     0.273 |  0.138 |   0     |   0.899 |
+-----------------------+---------+---------+-------+-----------+-----------+--------+---------+---------+
```

timings.py uses [curl](http://curl.haxx.se/) to make requests and generate timings. The following description of table columns is an adaptation of curl's [`--write-out` option](http://curl.haxx.se/docs/manpage.html).

* `sizeu` - The total amount of bytes that were uploaded.
* `sized` - The total amount of bytes that were downloaded.
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
  -c --fetch-count=COUNT  number of times to fetch each url [default: 1]
  -p --parallel           do requests in parallel
```
