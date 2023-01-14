import threading

"""1、准备一个函数"""
def my_func(a, b):
	print(a, b)

"""2、创建一个线程"""
t = threading.Thread(target=my_func, args=(100, 200))     #craw不加括号     元组要加括号

"""3、动线程"""
t.start()

"""4、等待线程结束（如果你在乎它什么时候结束）"""
t.join()
