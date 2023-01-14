import threading
import time

lock = Lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, number):
    with lock:  # 加锁保护
        if account.balance >= number:
            print(threading.current_thread().name, '取钱成功')
            # time.sleep(0.1)
            account.balance -= number
            print(threading.current_thread().name, '余额: ', account.balance)
        else:
            print(threading.current_thread().name, '余额不足')


if __name__ == '__main__':
    acc = Account(1000)
    ta = threading.Thread(name='ta', target=draw, args=(acc, 800))
    tb = threading.Thread(name='tb', target=draw, args=(acc, 800))

    ta.start()
    tb.start()
