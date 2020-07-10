def square_nums_gen(nums):
    for i in nums:
        yield i*i


def yield_xy():
    x = 5
    yield x
    y = 6
    yield y
    yield x + y


if __name__ == '__main__':
    iterator = square_nums_gen([1, 2, 3])

    print('square_nums_gen():')
    print(type(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))
    print()

    xy = yield_xy()
    print('yield_xy():')
    print(next(xy))
    print(next(xy))
    print(next(xy))
    # print(next(xy))
    print()

    print(next(yield_xy()))
    print(next(yield_xy()))
    print()

    for i in yield_xy():
        print(i)
