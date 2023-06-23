import pandas as pd 

data=pd.read_csv("t20.csv")
df= pd.DataFrame(data)
# print(df.head(10))
# print(df[[input(),input()]].head(10))
# print(df.loc[1:10])
print(df.loc[1:])
# print(df.loc[:10])
# print(df.loc[-100:])
# print(df.loc[:100,["Player","Runs"]])
# print(df.loc[:100,"Runs":])
# print(df.loc[:100,:"Runs"])
# print(df.loc[:100,"Runs":"SR"])
# print(df.iloc[:100,1:])
# print(df.iloc[:100,10:])
# print(df.iloc[:100,:-1])
# print(df.iloc[:100,:])
# print(df.iloc[:100,-4:-1])
# print(df.iloc[:100,10:-5])
# print(df.columns.values)
# fil=df.sort_values(df["Runs"])>5000
# print(fil)
# print(df.where(df.Player=="V Kohli (INDIA)"))
# print(df.where(df.Span>=2010))
# print(df.where(df.Span>=2010,"NA"))

# x=df.where(df.last==2019)
# print(df.dtypes)
print(df.query("Spam"))












