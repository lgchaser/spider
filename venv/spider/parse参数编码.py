# coding:utf8
from urllib import request, parse
'''
对url进行参数编码用到
parse模块
'''
if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("请输入你的关键字:")
    # 要利用数据，必须使用字典结构，而不能简单的wd=关键字
    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)

    print(qs)
    fullurl = url + qs

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)
