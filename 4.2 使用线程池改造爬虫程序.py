import concurrent.futures
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.cnblogs.com'
urls = [base_url+f'/#p{i}' for i in range(1, 51)]

def craw(url):          # 消费者
    response = requests.get(url)
    return  response.text

def parse(html):        #  生产者
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(craw, urls)
    htmls = list(zip(urls, htmls))
    for url, html in htmls:
        print(url, len(html))
print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(parse, html)
        futures[future] = url

    # for futrue, url in futures.items():			# 按入参顺序返回
    #     print(url, future.result())

    for future in concurrent.futures.as_completed(futures):		# 无序，先结束先返回
        url = futures[future]
        print(url, future.result())
print("parse over")
