import pandas as pd

d1 = pd.read_csv('../data/employees.csv')
d2 = pd.read_csv('../data/departments.csv')

d3 = d1.merge(d2, on='DeptID', how='inner')
d4 = d1.merge(d2, on='DeptID', how="outer")
d5 = d1.merge(d2, on='DeptID', how='right')
d6 = d1.merge(d2, how='cross')
print(d6)