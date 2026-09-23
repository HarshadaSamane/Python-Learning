import numpy as np
#Stacking

a = np.array([
  [1, 2],
  [3, 4]
])

b = np.array([
  [5, 6],
  [7, 8]
])

result1 = np.concatenate((a,b), axis = 0)
print(result1)

result2 = np.concatenate((a,b), axis = 1)
print(result2)

result3 = np.vstack((a,b))
print(result3)

result4 = np.hstack((a,b))
print(result4)

#Splitting

arr = np.array([10, 20, 30, 40, 50, 60])

# Split in 2 equal parts
result = np.split(arr,2)
print(result)

# Split in 3 equal parts
result = np.split(arr, 3)
print(result)

arr = np.array([
  [1, 2],
  [3, 4],
  [5, 6],
  [7, 8]
])

# Split in 2 parts using axis=0
result = np.split(arr, 2, axis=0)
print(result)