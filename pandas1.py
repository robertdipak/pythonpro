import pandas as pd
a=[5,7,2,2,8,9]
calories={"days1":420, "days2":380, "days3":390}
data={
    "calories":[420,512,460],
    "duration":[50,40,45]
}

myvar= pd.Series(a)
print(myvar[0])
myvar= pd.Series(a, index=["x","y","z","a","b","c"])
print(myvar["b"])
myvar= pd.Series(calories, index=["days1","days2"])
print(myvar)
myvar=pd.DataFrame(data)
print(myvar)
print(myvar.loc[1])
print(myvar.loc[[0,1]])
myvar=pd.DataFrame(data,index=["day1","day2","day3"])
print(myvar.loc["day2":])

