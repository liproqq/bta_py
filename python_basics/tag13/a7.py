import numpy as np

li = [[1,0,11],[2,13,5]]
arr = np.array(li)

print(arr)

arr2 = np.array([[1,5,8,4],
                [0,3,6,9],
                [4,7,9,2]])

print(arr2[1, 2])
print(arr2[1:, 2])
print(arr2[1, :2])

z = np.linspace(4, 18, 20)
print(z)