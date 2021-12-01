#!/usr/bin/python3
"""displays value of the variable X-Request-ID"""


if __name__ == '__main__':
    import sys
    import requests

    x = requests.get(sys.argv[1])

    data = x.headers

    print(data.get('X-Request-Id'))
