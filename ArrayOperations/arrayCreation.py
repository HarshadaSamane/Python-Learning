# 1D Array with 5 zeros

import numpy as np

arr = np.zeros(5)
print(arr)

# 3*4 array filled with ones
arr = np.ones((3,4))
print(arr)

# numbers from 10 to 20
arr = np.arange(10, 20)
print(arr)

# Even numbers from 2 to 20
arr = np.arange(2, 20, 2)
print(arr)

#2*3 array with value 5
arr = np.full((2,3),5)
print(arr)