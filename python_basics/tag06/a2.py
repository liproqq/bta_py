import functools as ft

# n!
n = int(input("Zahl: "))


def fac(x):
    return 1 if (x < 2) else x * fac(x-1)


print(fac(n))

print(ft.reduce(lambda x, y: x * y, range(1, n+1)))
