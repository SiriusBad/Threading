import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

PRIMES = [112272535095293] * 100
list = []
for i in range(100):
    list.append(i)

def is_prime(num,a):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    sqrt = int(math.floor(math.sqrt(num)))
    for i in range(3, sqrt + 1, 2):
        if num % i == 0: return False
    print(a)
    return True

def single_thread():
    for num in PRIMES:
        is_prime(num,1)
    print('single_thread is over')

def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES,list)
    print('multi_thread is over')

def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES,list)
    print('multi_process is over')

if __name__ == '__main__':
    start1 = time.time()
    single_thread()
    end1 = time.time()

    start2 = time.time()
    multi_thread()
    end2 = time.time()

    start3 = time.time()
    multi_process()
    end3 = time.time()

    print("Single Thread Costs: ", end1 - start1)
    print("Multi Thread Costs: ", end2 - start2)
    print("Multi Process Costs: ", end3 - start3)
