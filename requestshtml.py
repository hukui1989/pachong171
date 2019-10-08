import io
import json
from pprint import pprint

# from requests_html import HTMLSession
# session = HTMLSession()

# r = session.get('https://python.org/')
#
# # print(r.html.html)
#
# # 获取页面上的所有链接。
# all_links =  r.html.links
# # print(all_links)
# #
# # 获取页面上的所有链接，以绝对路径的方式。
# # all_absolute_links = r.html.absolute_links
# # print(all_absolute_links)
#
# w=r.html.find("h2.widget-title span")[0]
# # print(w.text)
# # print(w.attrs)
# print(w.attrs.get("aria-hidden"))
# w=r.html.find("h2.widget-title")[0]
# print(w.search("Get {}tarted")[0])
# print(w.html)
# print(list(map(lambda x : x.text,w)))

# print(r.html.xpath("//h2[@class='widget-title']/text()")[0])


# r=session.get("http://python-requests.org/")
# # print(r.apparent_encoding," ",r.encoding)
# rd=r.html.render()
# print(rd)

# r=session.get("https://job.dajie.com")
# print(r.html.html)
# for html in r.html:
#     print(html)
#     print("*********************************")

# from requests_html import HTML
# doc = """<a href='https://httpbin.org'>"""
# html=HTML(html=doc)
# # print(html.links)
# print(html.html)
# script = """
#         () => {
#             return {
#                 width: document.documentElement.clientWidth,
#                 height: document.documentElement.clientHeight,
#                 deviceScaleFactor: window.devicePixelRatio,
#             }
#         }
#     """
# h=html.render(script=script,reload=False)
# print(h)
# print("*****************")
# headers={
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"
#   }
# # ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
# r = session.get('http://httpbin.org/get',headers=headers)
# print(r.html.html)
# data={
#
# 'name': '15807118393',
# 'password': '1234asdf',
#
# }
# heards={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#     'Referer': 'https://accounts.douban.com/passport/login?source=main',
#     'Cookie': 'll="108288"; bid=jtxiFF1h7Ug; apiKey=; _pk_ses.100001.2fad=*; user_data={%22area_code%22:%22+86%22%2C%22number%22:%2215807118393%22%2C%22code%22:%221301%22}; vtoken=phone_register%200f5fec6458614390832f9868b7596b45; dbcl2="204436085:24txEyIGXH0"; ck=UX4x; ap_v=0,6.0; douban-fav-remind=1; last_login_way=account; push_noty_num=0; push_doumail_num=0; __utma=30149280.308335104.1569486496.1569486496.1569486496.1; __utmc=30149280; __utmz=30149280.1569486496.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmv=30149280.20443; __utmb=30149280.3.9.1569486496; _pk_id.100001.2fad=e2d1a8a4b715679e.1569485873.1.1569486508.1569485873.; login_start_time=1569486509645'
# }
# r = session.post('https://accounts.douban.com/j/mobile/login/basic', data=data)
# pprint(json.loads(r.html.html))



# from requests_html import HTMLSession
# session=HTMLSession()
# r=session.get("https://www.jianshu.com/u/7753478e1554")
# # print(type(r)," ",type(r.html)," ",type(r.html.html))
# r.html.render(scrolldown=50,sleep=1)
# titles = r.html.find('a.title')
# # print(titles)
# for i, title in enumerate(titles):
#     print(f'{i+1} [{title.text}](https://www.jianshu.com{title.links})')
#
# for i, title in enumerate(titles):
#     print(f'{i+1} [{title.text}](https://www.jianshu.com{title.attrs["href"]})')



from requests_html import HTMLSession

# 爬取天涯论坛帖子
url = 'http://bbs.tianya.cn/post-culture-488321-1.shtml'
session = HTMLSession()
r = session.get(url)
# 楼主名字
author = r.html.find('div.atl-info span a', first=True).text
# 总页数
div = r.html.find('div.atl-pages', first=True)
links = div.find('a')

total_page = 1 if links == [] else int(links[-2].text)
# 标题
# print(total_page )
title = r.html.find('span.s_title span', first=True).text

with open(f'{title}.txt', 'a+', encoding='utf-8') as f:
    for i in range(1, total_page + 1):
        # s = url.rfind('-')
        # print(str(s) + "**************")
        url = 'http://bbs.tianya.cn/post-culture-488321-'+str(i)+'.shtml'
        r = session.get(url=url)
        # 从剩下的里面找楼主的帖子
        items = r.html.find(f'div.atl-item[_host={author}]')
        # print(items)
        for item in items:
            content: str = item.find('div.bbs-content', first=True).text
            # 去掉回复
            if not content.startswith('@'):
                f.write(content + "\n")
                print("写入成功")
