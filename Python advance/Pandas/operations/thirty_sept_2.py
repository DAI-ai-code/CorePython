import pandas as pd
from numpy.lib.recfunctions import join_by

d1 = pd.read_csv("../data/employees.csv")
d2 = pd.read_csv("../data/departments.csv")

d3 = d1.merge(d2, on='DeptID', how="inner")
print(d3)
print("-----------------")
dept_grps = d3.groupby("DepartmentName")
highest_salary = dept_grps["Salary"].max()
print(highest_salary)
print("-----------------")
dept_count = dept_grps["EmployeeID"].count()
print(dept_count)
print("-----------------")
for i,k in dept_grps["Salary"]:
    print(i, " ", k.mean())

