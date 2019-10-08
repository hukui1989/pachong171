# GET请求
from urllib import request as ur

url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&_v=0.38498314&x-zp-page-request-id=4aea81ef10fa4b6aabf8319073c0ebf0-1567999305242-790668&x-zp-client-id=55724e1f-bf4a-41b6-895d-26f229442f8d'

r = ur.urlopen(url)
print(r.read().decode('utf-8'))

# POST请求
# from urllib import request as ur
# from urllib import parse
# import json
#
# url = 'https://www.iqianyue.com/mypost'
#
# data = {
#     'name': 'zhengbao',
#     'pass': '123'
# }
# p = parse.urlencode(data)
# p = bytes(p,encoding='utf-8')
#
# r = ur.urlopen(url,data=p)
# print(r.read().decode())
# 生成了一个Request对象，并且发送出去