import pandas as pd

l = [1,2,3,"4"]
x  = pd.Series(l, index=["one","two","three","4"])
print(x)