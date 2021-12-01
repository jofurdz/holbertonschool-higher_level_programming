#!/usr/bin/python3
"""takes in URL, sends request and displays value"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print('{}'.format(html.get('X-Request-Id')))
