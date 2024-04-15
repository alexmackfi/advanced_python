import threading
from threading import Thread
import time
from multiprocessing import Pool, Queue, Pipe, Process
import codecs
from datetime import datetime

def fib(n):
    if n > 2:
        return (fib(n - 1) + fib(n - 2))
    else:
        return 1

def one_thread_fib(n):
    start = time.time()
    res = fib(n)
    end = time.time()
    print(f"synchronous run in {end - start} seconds")

def many_threads_fib(n, numb_t):
    threads_list = []
    start = time.time()
    for i in range(numb_t):
        t = Thread(name = "fibonacci", target=fib, args=(n, ))
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()

    # while any(t.is_alive() for t in threading.enumerate() if t.name == 'fibonacci'):
    #     pass
    end = time.time()
    print(f"{numb_t} threads run in {end - start} seconds")

def many_process_fib(n, numb_p):
    start = time.time()
    with Pool(numb_p) as pool:
        res = pool.map(fib, (n,))
    end = time.time()
    print(f"{numb_p} processes run in {end - start} seconds")
