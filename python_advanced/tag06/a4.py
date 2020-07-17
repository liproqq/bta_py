import numpy as np

arr = np.random.randint(1, 6, size=(5, 3))

print(arr)
print("Mean:", arr.mean())

print("Aufgabe")
print(np.any(arr == np.floor(arr.mean())))

# print("Bonus 1")
# for i in range(arr.shape[0]):
#     print(i, np.any(arr[i] == np.floor(arr.mean())))

print("Bonus 1")
print(np.any(arr == np.floor(arr.mean()), axis=1))

print("Bonus 2")
print(np.all(np.isclose(arr.mean(), arr, atol=1), axis=0))
