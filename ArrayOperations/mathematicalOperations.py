import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Total of all elements
print(arr.sum())

# Average
print(arr.mean())

# Minimum Value
print(arr.min())

# Maximum Value
print(arr.max())

# Sum of each column
print(np.sum(arr, axis=0))

# Sum of each row
print(np.sum(arr, axis=1))