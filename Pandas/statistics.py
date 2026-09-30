import pandas as pd 

data = {
  "Name": ["Harshada", "Amit", "Priya", "Rahul", "Sneha"],
  "Age" : [23, 24, 22, 25, 23],
  "Marks" : [85, 78, 92, 69, 88]
}

df = pd.DataFrame(data)

#average Age
print(df["Age"].mean())

#Total Marks
print(df["Marks"].sum())

#highest Marks
print(df["Marks"].max())

#lowest marks
print(df["Marks"].min())

#median marks
print(df["Marks"].median())

#Use describe
print(df.describe())
