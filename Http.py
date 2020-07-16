import requests


def getHttp(url):
    r = requests.get(url)
    r.text.encode('utf-8')
    return r.text
