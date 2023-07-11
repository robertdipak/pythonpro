import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("billionaires.csv")
# print(data.head(10))
result=data.describe()
result=data.columns
result=data.year
print(result)