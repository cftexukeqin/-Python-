import requests
from bs4 import BeautifulSoup as bs
import re
headers = {
    'Host': 'sou.zhaopin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Referer': 'http://www.zhaopin.com/xian/',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache, no-store, max-age=0',
}
req = requests.get('http://sou.zhaopin.com/jobs/searchresult.ashx?jl=854&kw=python&sm=0&p=1',headers=headers)
req.encoding = 'utf-8'
soup = bs(req.text,'html.parser')
titles = soup.select(".zwmc a")
position = []
for i in titles:
    position.append(i.text)
# print(position)
company_names = soup.select('.gsmc a')
company_lists = []
for j in company_names:
    company_lists.append(j.text)
# print(company_lists)
money = soup.select('.zwyx')
money_lists = []
for l in money:
    money_lists.append(l.text)
# print(money_lists)
for i,j,l in zip(company_lists,position,money_lists):
    print(i,j,l)

