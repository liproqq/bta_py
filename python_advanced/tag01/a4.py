import random


def count_random(a, b):
    x = 0
    while True:
        x += random.randint(a, b)
        yield x


counter = count_random(5, 55)

print(next(counter))
