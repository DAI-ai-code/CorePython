import numpy as np

x = np.array([[1, 'abc', 9900], [2, 'bcd', 20202]])
for i in x:
    if i[0] == '1':
        print(i)