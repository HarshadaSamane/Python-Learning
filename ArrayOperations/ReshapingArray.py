import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Reshape in 2*4
new_arr1 = arr.reshape(2, 4)
print(new_arr1)

# 4*2
new_arr2 = arr.reshape(4, 2)
print(new_arr2)

# 2 rows
new_arr3 = arr.reshape(2, -1)
print(new_arr3)

# 3*3
new_arr4 = arr.reshape(3, 3)
print(new_arr4)
# ValueError: cannot reshape array of size 8 into shape (3,3)


# Flatten the array
arr = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
])

print(arr.shape)

flat  = arr.flatten()
print(flat)

print(flat.shape)

flat1 = arr.reshape(-1)
print(flat1)


