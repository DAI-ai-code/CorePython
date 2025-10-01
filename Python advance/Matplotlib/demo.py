import  matplotlib.pyplot as plt
import pandas as pd

empname = ['abc', 'mno', 'xyz', 'pqr']
salary = [99000, 45000, 25000, 78000]

# plt.scatter(empname, salary)
# plt.show()

df = pd.read_csv('./data/orbital_swarm_1000.csv')

plt.scatter(df['Orbital_Radius'], df['Energy_Level'], marker='.', c=df['Cluster_ID'], s=20*df['Energy_Level'])
plt.show()
