import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# df = pd.read_csv('./inputs/weatherAUS (testdata).csv')

X = np.array(1,10)
Y = X*5

plt.figure((12,8), facecolor="#000000", edgecolor="#000000", frameon=False)

plt.plot([X,Y,'r'])
plt.show()