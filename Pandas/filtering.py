import pandas as pd 

data = {
  "Name": ["Harshada", "Amit", "Priya", "Rahul", "Sneha"],
  "Age" : [23, 24, 22, 25, 23],
  "Marks" : [85, 78, 92, 69, 88]
}

df = pd.DataFrame(data)

#Students whos marks are greater than 80
result = df[df["Marks"]>80]
print(result)

#marks less than 80
result = df[df["Marks"]<80]
print(result)

#marks btn 75 & 90
result = df[(df["Marks"]>=75)&(df["Marks"]<=90)]
print(result)

#age 23
result = df[df["Age"]==23]
print(result)

# marks > 80 and age = 23
result = df[(df["Marks"]>80) & (df["Age"]==23)]
print(result)

#marks > 90 or age = 25
result = df[(df["Marks"]>90) | (df["Age"]==25)]
print(result)









