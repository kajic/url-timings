"""timings.py

Usage:
  timings.py [--urls=URLS] [--fetch-count=COUNT] [--parallel]
  timings.py --version

Options:
  -h --help               show this help message and exit
  -v --version            show version and exit
  -u --urls=URLS          path to urls file (one url per line)
  -c --fetch-count=COUNT  number of times to fetch each url [default: 1]
  -p --parallel           do requests in parallel
"""
import sys
import json
import re
from collections import defaultdict
from subprocess import PIPE

import gevent
from docopt import docopt
from tabulate import tabulate

arguments = docopt(__doc__, version='0.1')
urls_filename = arguments['--urls']
fetch_count = int(arguments['--fetch-count'])
parallel = arguments['--parallel']

if parallel:
    from gevent.subprocess import Popen
else:
    from subprocess import Popen

def urls(filename):
    with open(filename, 'r') as f:
        return [url.strip() for url in f]

def fetch(url):
    sys.stdout.write(".")
    sys.stdout.flush()

    p = Popen(['curl', '-w', '@curl-format.txt', '-o', '/dev/null', '-s', url], stdout=PIPE)
    out, err = p.communicate()
    out = re.sub(r'(\d+),(\d+)', r'\1.\2', out)
    return json.loads(out)

def list_of_dict_avg(l):
    d_sum = defaultdict(int)
    for d in l:
        for key in d.keys():
            d_sum[key] += d[key]

    d_avg = {}
    for key in d_sum.keys():
        d_avg[key] = d_sum[key]/float(len(l))

    return d_avg

def fetch_avg(url, n):
    jobs = [gevent.spawn(fetch, url) for i in range(n)]
    gevent.joinall(jobs, timeout=120)
    results = [job.value for job in jobs]
    return list_of_dict_avg(results)

def format(stats_list):
    cols = ['url', 'sizeu', 'sized', 'dns', 'tcp_con', 'ssl_con', 'calc', 'trans', 'total']
    def row(url, stats):
        ssl_con = stats['time_appconnect']-stats['time_connect'] if stats['time_appconnect'] else 0
        return [
            url[:100],
            stats['size_request']+stats['size_upload'], # sizeu
            stats['size_download']+stats['size_header'], # sized
            stats['time_namelookup']-stats['time_redirect'], # dns
            stats['time_connect']-stats['time_namelookup'], # tcp_con
            ssl_con,
            stats['time_starttransfer']-stats['time_pretransfer'], # calc
            stats['time_total']-stats['time_starttransfer'], # trans
            stats['time_total']
        ]
    rows = [row(url, stats) for url, stats in stats_list]
    return tabulate(rows, cols, tablefmt="grid")

stats = []
for url in urls(urls_filename):
    stats.append((url, fetch_avg(url, fetch_count)))

print ""
print format(stats)
