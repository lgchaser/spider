# coding:utf8
import json
from urllib import request, parse
'''
1.利用data构造内容，然后urlopen打开；
2.返回一个json格式的结果
3.json解码，得到结果
'''
keyword = input('请输入翻译的单词：')

baseurl = 'https://fanyi.baidu.com/sug'

data = {
       'kw': keyword
    }
print(data)

data = parse.urlencode(data).encode('utf8')
# 这里urlencode编码之后是str格式，我们需要将他用encode编码成字节流(bytes）
headers = {
        'Content-Length': len(data)
    }

req = request.Request(url=baseurl, data=data, headers=headers)
rsp = request.urlopen(req)
json_data = rsp.read().decode('utf8')

print(type(json_data))
print(json_data)


# 这里得到得json_data是str格式，需要通过json模块得load方法装载成字典dict
json_data = json.loads(json_data)
print(type(json_data))

for item in json_data['data']:
    print(item['k'], "---", item['v'])


