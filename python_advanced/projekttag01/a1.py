def fib():
    seq = [0, 1]
    while True:

        yield seq[1]
        seq = [seq[1], sum(seq)]


fib_seq = fib()

for entry in range(10):
    print(next(fib_seq))
