class My_Range():
    def __init__(self, start, end):
        self.start = start
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            self.value = self.start
            raise StopIteration
        current = self.value
        self.value += 1

        return current


class My_Range2():
    def __init__(self, start, end):
        self.start = start
        self.value = start
        self.end = end

    def __iter__(self):
        return self.My_Iterator(self.start, self.end)

    class My_Iterator:
        def __init__(self, start, end):
            self.start = start
            self.value = start
            self.end = end

        def __next__(self):
            if self.value > self.end:
                raise StopIteration
            current = self.value
            self.value += 1

            return current


if __name__ == "__main__":
    my_iter = My_Range(0, 4)
    print(f"\n\nMy_range:")
    print("Erster For-Loop")
    for i in my_iter:
        print(i)
    print("Zweiter For-Loop")
    for i in my_iter:
        print(i)

    my_iter2 = My_Range2(0, 4)
    print(f"\n\nMy_Range2:")
    print("Erster For-Loop")
    for i in my_iter2:
        print(i)
    print("Zweiter For-Loop")
    for i in my_iter2:
        print(i)
