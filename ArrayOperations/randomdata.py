import numpy as np

arr = np.random.randint(1,50, size=10)
print(arr)

arr = np.random.randint(10, 99, size=(3,3))
print(arr)

arr = np.random.rand(5)
print(arr)

languages = np.array(["Python", "Java", "C#", "JavaScript"])
print(np.random.choice(languages))