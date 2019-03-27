# coding:utf8
import chardet
from urllib import request
if __name__ == '__main__':
    url ="https://jobs.zhaopin.com/CC388089689J00345953301.htm"
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    print(type(html))
    html = html.decode(cs.get("enconding", "utf-8"))
    print(type(cs.get("enconding", "utf-8")))
    print(html)

