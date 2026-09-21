import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

print(type(numbers))

print(numbers[0])
print(numbers[-1])
numbers[2] = 35
print(numbers[0:4])
print(numbers + 10)
print(numbers * 3)