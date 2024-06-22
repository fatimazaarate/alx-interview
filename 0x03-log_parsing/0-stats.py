#!/usr/bin/python3
"""function that processes log entries """

import sys
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_size = [0]


def print_metrics():
    print("File size: {}".format(sum(total_size)))
    for code, count in sorted(status.items()):
        if count:
            print("{}: {}".format(code, count))


try:
    for a, line in enumerate(sys.stdin, start=1):
        alike = line.rstrip().split()
        try:
            code_status = alike[-2]
            size = alike[-1]
            if code_status in status.keys():
                status[code_status] += 1
            total_size.append(int(size))
        except Exception:
            pass
        if a % 10 == 0:
            print_metrics()
    print_metrics()
except KeyboardInterrupt:
    print_metrics()
    raise
