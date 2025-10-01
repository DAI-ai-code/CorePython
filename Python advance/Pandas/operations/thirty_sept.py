from datetime import datetime

import pandas as pd

df = pd.read_csv("../data/data.csv")
# df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df)

# df["City"].fillna("America", inplace=True)
# print(df)

df.fillna({"Enrollment_Date": datetime.today().strftime('%Y-%m-%d')}, inplace=True)
# print(df)

y = df.groupby('City')
print(y)
print(y.groups)
print(y.get_group('New York'))
