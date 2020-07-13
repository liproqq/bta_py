import numpy as np

from multiprocessing import Process, Pipe


def square(conn):
    for i in range(10):
        x = conn.recv()
        conn.send(x**2)


def root(conn):
    for i in range(10):
        x = conn.recv()
        conn.send(np.sqrt(x))


if __name__ == '__main__':
    conn_square, conn_square_main = Pipe()
    conn_root, conn_root_main = Pipe()

    p_square = Process(target=square, args=[conn_square])
    p_root = Process(target=root, args=[conn_root])

    p_square.start()
    p_root.start()

    nums = np.random.randint(10, 101, 10)
    print(nums)

    # Übergabe der Parameter an die Prozessse
    for num in nums:
        conn_root_main.send(num)
        conn_square_main.send(num)

    # Abholen der Ergebnisse
    squares = []
    roots = []
    for i in range(10):
        squares.append(conn_square_main.recv())
        roots.append(conn_root_main.recv())
