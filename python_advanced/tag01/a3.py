def count_gen(max):
    current = 0
    while current <= max:
        yield current
        current += 0.5


counter = count_gen(5)

for i in counter:
    print(i)
