#!/usr/bin/python3
"""takes in URL and displays the body of th response"""


if __name__ == '__main__':
    from sys import argv
    import requests

    request = requests.get(argv[1])

    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
