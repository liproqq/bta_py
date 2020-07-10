import numpy as np
from time import sleep
from multiprocessing import Process, current_process


def sum2(*args):
    sleep(0.5)

    print(f"current process: {current_process().pid} {sum(args)}")


if __name__ == "__main__":
    num = np.random.randint(0, 100, (10, 2))

    for i in num:
        process = Process(target=sum2, args=i)
        process.start()
