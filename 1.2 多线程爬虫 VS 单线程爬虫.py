import requests
import time
import threading

base_url = 'https://www.cnblogs.com'
urls = [base_url + f'/#p{i}' for i in range(1, 51)]


def craw(url):
    response = requests.get(url)
    print(url, len(response.text))


def single_thread():
    for url in urls:
        craw(url)


def multi_thread():
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))    #craw不加括号     元组要加括号
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("Single Thread Crawling Cost", end - start, "seconds.")

    start = time.time()
    multi_thread()
    end = time.time()
    print("Multi Thread Crawling Cost", end - start, "seconds.")
