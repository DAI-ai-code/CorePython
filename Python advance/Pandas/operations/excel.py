import pandas as pd
d = pd.read_excel("../data/excel.xlsx",sheet_name=0)
index = ['one', 'two', 'three', 'four']
df = d.iloc[:4]
df.index = index
print(df)
print(df.loc['two'])
# print(d.info())
# print(d[d["Country"]=="Norway"])
x = d.iloc()
y = d[d["Country"]=="Norway"]

# print(d.loc[140])

# for i in y:
    # print(i, y[i].values[0])
