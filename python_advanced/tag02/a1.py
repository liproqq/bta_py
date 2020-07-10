import os
from time import sleep
from multiprocessing import Pool


def func(x):
    sleep(0.3)
    return x + 1


if __name__ == "__main__":
    p = Pool(processes=4)
    result = p.map(func, range(50))
    print(result)
