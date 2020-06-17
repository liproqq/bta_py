from turtle import *


left(90)


def baum(x):
    if x < 3:
        return
    forward(x)
    right(45)
    baum(x/2)
    left(90)
    baum(x/2)
    right(45)
    back(x)

baum(100)

done()
