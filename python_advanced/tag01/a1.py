class My_Range():
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1

        return current


if __name__ == "__main__":
    my_iter = My_Range(1, 4)
    my_list = [1, 2, 3]

    print(type(iter(my_iter)))
    print(type(iter(my_list)))

    list_iterator = iter(my_list)

    print(f"Liste: {my_list}")
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    # print(next(list_iterator))

    print(f"\n\nMy_range: {my_iter}")
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

    my_iter = My_Range(1, 4)
    print("for-loop:")
    for i in my_iter:
        print(i)

    for i in my_iter:
        print(i)

    print(f"my_iter.value: {my_iter.value}")
