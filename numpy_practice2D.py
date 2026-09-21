import numpy as np

numbers = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
])

print(numbers[1, 1])
print(numbers[0,2])
print(numbers[2,0])

numbers[2,1] = 85
print(numbers)

print(numbers.shape)

print(numbers[1, : ])
print(numbers[:, 2])
print(numbers[0:2, :])
print(numbers[0:2, 1:])