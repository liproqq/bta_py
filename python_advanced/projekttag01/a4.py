from multiprocessing import (Process, Lock, Value,
                             current_process, active_children)
from time import sleep, time
from random import randint


def stackingRobot(delay, amount, lock, stack):
    for i in range(amount):
        with lock:
            sleep(delay)
            stack.value += 1
            print(stack.value, current_process().pid)


def orderRobot(lock, stack):
    while True:
        sleep(0.1)
        with lock:
            if stack.value > 11:
                stack.value -= 7
                print("ORDER ORDER ORDER")


if __name__ == "__main__":
    stack = Value("i")
    lock = Lock()
    robot1 = Process(target=stackingRobot,
                     args=(0.2, randint(15, 25), lock, stack))
    robot2 = Process(target=stackingRobot,
                     args=(0.3, randint(15, 25), lock, stack))

    robot3 = Process(target=orderRobot, args=(lock, stack), daemon=True)

    robot1.start()
    robot2.start()
    robot3.start()

    robot1.join()
    robot2.join()

    print("end:", stack.value)
