import requests
import time
import threading
import queue
from bs4 import BeautifulSoup
import random

"""以下生产者 craw 爬取页面并将返回的 html 放到 html_queue，
消费者 parse 从 html_queue 中取得 html ，解析，并将结果存入到文件中。"""

base_url = 'https://www.cnblogs.com'
urls = [base_url + f'/#p{i}' for i in range(1, 51)]


def craw(url):  # 消费者
    response = requests.get(url)
    return response.text


def parse(html):  # 生产者
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size = ", url_queue.qsize())
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            fout.write(str(result) + '\n')
        print(threading.current_thread().name, f"results.size {len(results)}",
              "html_queue.size = ", html_queue.qsize())
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(
            target=do_craw, args=(url_queue, html_queue), name=f"craw {idx}"
        )
        t.start()
    fout = open('result.txt', 'w')
    for idx in range(2):
        t = threading.Thread(
            target=do_parse, args=(html_queue, fout), name=f"parse {idx}"
        )
        t.start()

"""可以看到，由于生产者有3个线程，消费者有2个线程，即页面的爬取比解析的要快，
故 html_queue 中的元素个数有升有降，但总体是在增加。
最终生产者已经将 url_queue 中的 url 全部爬取完毕，随后消费者才将 html_queue 中的 html 全部解析。"""

