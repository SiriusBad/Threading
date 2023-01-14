from concurrent.futures import ThreadPoolExecutor
import concurrent


"""
使用线程池的好处：

    提升性能：省去大量新建、终止线程的开销，重用了线程资源
    防御功能：能够有效避免因为创建线程过多，而导致系统符合过大而响应变慢的问题
    代码优势：使用线程池的语法相比于自己新建线程执行线程更加简洁
    使用场景：适合处理突发性大量请求或需要大量线程完成任务，但实际任务处理时间较短
"""

def craw(url):
    print(url)
urls = ['https://www.baidu.com/s?ie=utf-8&f=','https://www.baidu.com']

"""用法1：map"""
with ThreadPoolExecutor() as pool:
    pool.map(craw, urls)

"""用法2：future"""
with ThreadPoolExecutor() as pool:
    futures = [pool.submit(craw, url) for url in urls]

    for future in futures:
        print(future.result())
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

"""future模式，更强大，注意
as_completed包裹执行的话会先完成，先返回，而非按照入参的顺序，是否要用
as_completed需要看实际情况。"""
