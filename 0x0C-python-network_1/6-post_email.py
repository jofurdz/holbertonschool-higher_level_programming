#!/usr/bin/python3
"""sends an email"""


if __name__ == '__main__':
    from sys import argv
    import requests

    newDict = {}
    newDict['email'] = argv[2]
    request = requests.post(argv[1], newDict)
    print(requests.text)
