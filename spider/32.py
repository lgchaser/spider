# coding:utf8
from urllib import request, error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
    except Excepetion as e:
        print(e)
