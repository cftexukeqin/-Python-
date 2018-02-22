import requests
import pandas
from bs4 import BeautifulSoup as bs


def get_info(url):
    headers = {
        'Host': 'detail.zol.com.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    soup = bs(res.text, 'html.parser')
    title_list = []
    price_list = []
    star_list = []
    titles = soup.select('.pro-intro h3')
    for title in titles:
        title_list.append(title.text)
    prices = soup.select('.price-type')
    for price in prices:
        price_list.append(price.text)
    stars = soup.select('.grade b')
    for star in stars:
        star_list.append(star.text)
    lists = list(zip(title_list, star_list, price_list))
    return lists


if __name__ == '__main__':
    total_lists = []
    url = 'http://detail.zol.com.cn/memory/s3722_p3299/shanxi/{}.html'
    for i in range(1, 7):
        rel_url = url.format(i)
        total_lists.extend(get_info(rel_url))
    df = pandas.DataFrame(total_lists, columns=['名称', '性价比', '报价'])
    df.to_excel('内存条DDR3.xlsx')
    print('Spider Over')

