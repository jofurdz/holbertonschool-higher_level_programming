#!/usr/bin/python3
"""takes in URL and email and sends a POST request to the passed URL"""


if __name__ == '__main__':
    import sys
    from urllib import request, parse

    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode("UTF-8")
    req = request.Request(sys.argv[1], email)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode("UTF-8"))
