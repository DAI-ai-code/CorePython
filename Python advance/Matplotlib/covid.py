import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.chart import label

# Set display options to show everything
pd.set_option('display.max_rows', None)      # Show all rows
pd.set_option('display.max_columns', None)   # Show all columns
pd.set_option('display.width', None)         # No line wrapping
pd.set_option('display.max_colwidth', None)  # Show full content of each cell

df = pd.read_csv("./data/worldometer_data.csv")
# print(df["TotalDeaths"].nlargest(5))
print(df.iloc[df["TotalDeaths"].nlargest(5).index]["Country/Region"])
x = df.iloc[df["TotalDeaths"].nlargest(5).index]["Country/Region"]
y = df.iloc[df["TotalDeaths"].nlargest(5).index]["TotalCases"]
y2 = df.iloc[df["TotalDeaths"].nlargest(5).index]["TotalDeaths"]
plt.plot(x,y,label="Total cases")
plt.plot(x,y2*10,label="Deaths * 50")
plt.legend()
plt.xlabel("Country/Region")
plt.ylabel("Count")
plt.show()