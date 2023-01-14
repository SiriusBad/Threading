import threading

"""线程安全指的是某个函数、函数库在多线程环境中被调用时，能够正确地处理多个线程间的的共享变量，是程序功能正确完成。

由于线程的执行随时会发生切换，就会造成不可预料的后果，出现线程的不安全。

注意线程并发不安全的问题只有在线程切换时机恰好导致了数据竞争时才会出现，也就是说有时会出现，有时又不会出现。
"""

"""
用法1：try-finally 模式

lock = threading.Lock()
lock.acquire()
try:
  # do something
finally:
	lock,release()
"""

"""
用法2：with模式

lock = threading.Lock()
with lock:
  # do something
"""
