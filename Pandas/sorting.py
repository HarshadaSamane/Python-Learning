import pandas as pd 

data = {
  "Name": ["Harshada", "Amit", "Priya", "Rahul", "Sneha"],
  "Age" : [23, 24, 22, 25, 23],
  "Marks" : [85, 78, 92, 69, 88]
}

df = pd.DataFrame(data)

#Sort marks low to high
result = df.sort_values("Marks")
print(result)

#high to low
result = df.sort_values("Marks", ascending=False)
print(result)

#Age-> young to old
result = df.sort_values("Age")
print(result)

#First Age then Marks
result = df.sort_values(["Age", "Marks"])
print(result)