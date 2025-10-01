# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import subplot
#
# df = pd.read_csv('./data/emp.csv')
# df = df.head()
# plt.subplot(1,2,1)
# plt.plot(df['Name'],df['Salary'], marker='o', color='red')
# plt.grid(True)
#
# plt.subplot(1,2,2)
# ename = ["aa","bb","cc","dd","ee"]
# esala = [10000,20000,30000,50000,30000]
# plt.plot(ename,esala,marker='x',color='blue')
#
# plt.subplot(2,2,1)
# ename = ["aa","bb","cc","dd","ee"]
# esala = [10000,20000,30000,50000,30000]
# plt.plot(ename,esala,marker='x',color='blue')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/emp.csv')
df = df.head()

plt.subplot(2,2,1)
plt.plot(df['Name'], df['Salary'], marker='o', color='red')
plt.grid(True)
plt.title('Employee Salaries')
plt.xticks(rotation=45)

plt.subplot(2,2,2)
ename = ["aa","bb","cc","dd","ee"]
esala = [10000,20000,30000,50000,30000]
plt.plot(ename, esala, marker='x', color='blue')
plt.title('Custom Data 1')

plt.subplot(2,2,3)
ename = ["aa","bb","cc","dd","ee"]
esala = [10000,20000,30000,50000,30000]
plt.plot(ename, esala, marker='x', color='green')
plt.title('Custom Data 2')

# Add space between rows
plt.subplots_adjust(hspace=0.5, wspace=0.3)  # hspace = vertical gap, wspace = horizontal gap
plt.show()