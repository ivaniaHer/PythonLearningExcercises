import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import read_csv

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x,y)
plt.show()

# pandas & matplotlib
df = pd.read_csv('personas.csv')
df["pais"].value_counts().plot(kind='bar')
plt.title("Cantidad de personas por país")
plt.show()