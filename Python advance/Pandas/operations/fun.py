import pandas as pd
df = pd.read_csv("../data/dataset.csv")
pd.set_option('display.max_columns', None)
# print(df)

print(df.iloc[0])