import pandas as pd
import matplotlib.pyplot as plt

file = open('sirlog.log', 'r')
file.readlines()
df = pd.read_table('sirlog.log', header=None)
new_df = pd.DataFrame()
new_df['DateTime'] = df[0].map(lambda x: x.split(" [")[0])
new_df['Level'] = df[0].map(lambda x: x.split(" ")[2].strip("[").strip("]"))
new_df['Message'] = df[0].map(lambda x: x.split("- ")[1].strip())
l = new_df["Level"].value_counts().values
print(l)
plt.pie(l)
plt.show()

# print(new_df)
