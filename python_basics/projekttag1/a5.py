# Die Fibonacci-Folge ist:
# 0, 1, 1, 2, 3, 5, 8, 13,...
# Das nächste Element berechnet sich immer aus dem Produkt der zwei Vorgänger.
# (Bis auf die ersten zwei Elemente, die 0 und 1 sind.)
# 0. Element = 0
# 1. Element = 1
# 2. Element = 0+ 1 = 1
# 3. Element = 1 + 1 = 2
# 4. Element = 1 + 2 = 3
# 5.Element = 2 + 3 = 5
# 6.Element = 3 + 5 = 8
# 7. Element = 5 + 8 = 13
# ...
# n. Element = n-1. Element + n-2. Element
# https://de.wikipedia.org/wiki/Fibonacci-Folge
# 1) Berechne die Fibonacci-Folge bis zum n. Element. (n wird eingelesen)
# 2) Berechne die Fibonacci-Folge bis zum n. Element rekursiv.

import time

seq_len = 33

t0 = time.time()


def fib_seq(n):
    seq = [0, 1]

    for i in range(2, n+1):
        seq.append(seq[-2]+seq[-1])
    return seq


print(fib_seq(seq_len))
print(time.time()-t0)

t1 = time.time()


def rec_fib(n):
    return n if n < 2 else (rec_fib(n-1)+rec_fib(n-2))


def rec_seq(x):
    rec_seq = []
    for i in range(x):
        rec_seq.append(rec_fib(i))
    return rec_seq


print(rec_seq(seq_len))
print(time.time()-t1)
