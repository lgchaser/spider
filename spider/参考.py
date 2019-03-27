import urllib.request
import urllib.parse
import json
content = input("请输入需要翻译的内容：")
url = 'http://fanyi.baidu.com/v2transapi'
data = {
    'from': 'en',
    'to': 'zh',
    'query': content,
    'transtype': 'trans',
    'simple_means_flag': '3'}
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
#print(len(html))
#print(html)
target = json.loads(html)

print(target['result']['data'][0]['dst'])
