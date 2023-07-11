import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

data= pd.read_csv("t20.csv")
df=pd.DataFrame(data)
N=3000
menMeans=(20,35,30,35,27)
womenMeans=(25,35,62,85,65)
ind=np.arange(N)
width=0.35
fig=plt.figure()
ax=fig.add_axes(df["Player"])
plt.show()
