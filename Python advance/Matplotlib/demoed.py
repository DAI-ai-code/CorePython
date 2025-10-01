import  matplotlib.pyplot as plt
import pandas as pd

empname = ['abc', 'mno', 'xyz', 'pqr']
salary = [99000, 45000, 25000, 78000]
dummy = [1, 1, 1, 1, 4, 5, 5, 3, 3, 2]
# dummy = [count * [i] for i, count in enumerate(range(50, 40, -1), start=40)]
print(dummy)
plt.hist(dummy)
plt.pie(salary)
plt.show()