from threading import Lock, Thread
from time import time

counter = 1000000


def one_up_lock(lock):
    start = time()
    i = 0
    for _ in range(counter):
        with lock:
            i += 1
    print("Lock:", time() - start)


def one_up():
    start = time()
    i = 0
    for _ in range(counter):
        i += 1
    print("No lock:", time() - start)


lock = Lock()

a = Thread(target=one_up_lock, args=[lock])
b = Thread(target=one_up)

a.start()
b.start()
