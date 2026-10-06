import pandas as pd

data = {
  "Name" : ["Harshada", "Amit", "Priya", "Rahul", "Sneha"],
  "Age" : [23, 24, 22, 25, 23],
  "Marks" : [85, 78, 92, 69, 88]
}

df = pd.DataFrame(data)

# 1 Add City Column
df["city"] = ["Pune", "Mumbai", "Pune", "Nashik", "Pune"]

# 2 Add Passes Column
df["Passed"] = df["Marks"] >= 40

# 3 Add Bonus Marks
df["BonusMarks"] = 5

# 4 Final Marks
df["FinalMarks"] = df["Marks"] + df["BonusMarks"]

# 5 Print final df
print(df)


#Deleting the data
import pandas as pd

data = {
  "Name" : ["Harshada", "Amit", "Priya", "Rahul", "Sneha"],
  "Age" : [23, 24, 22, 25, 23],
  "Marks" : [85, 78, 92, 69, 88],
  "City" : ["Pune", "Mumbai", "Pune", "Nashik", "Pune"]
}

df = pd.DataFrame(data)

# 1 delete City Column
df = df.drop("City", axis = 1)

# 2 delete Age Column
df = df.drop("Age", axis = 1)

# 3 remove row of index 3
df = df.drop(3, axis = 0)

# 4 remove index 1 and 4
df = df.drop([1,4], axis = 0)

print(df)