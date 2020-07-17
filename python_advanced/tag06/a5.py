import numpy as np
from pprint import pprint as print

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

name_type = {"names": ("name", "age", "weight"),
             "formats": ("U10", "i4", "f8")}

data = np.zeros(4, dtype=name_type)

data["name"] = name
data["age"] = age
data["weight"] = weight

print(data)
