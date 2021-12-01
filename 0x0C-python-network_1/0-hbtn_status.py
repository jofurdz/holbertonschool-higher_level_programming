#!/usr/bin/python3
"""fetches URL"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(str(html)))
        HTMLdecode = html.decode('UTF-8')
        print('\t- utf8 content: {}'.format(HTMLdecode))
