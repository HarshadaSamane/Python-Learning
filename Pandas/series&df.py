import pandas as pd

marks = pd.Series([75, 82, 91, 68, 88])

print(marks)

print(marks[2])

# Data Farme
data = {
  "Name" : ["Harshada", "Amit", "Priya", "Rahul"],
  "Age" : [23, 24, 22, 25],
  "Marks" : [85, 78, 92, 69]
}

df = pd.DataFrame(data)
print(df)