import pandas as pd 
technologies={
    "Course":["Spark","PySpark","Python","Pandas"],
    "Fee":[20000,30000,40000,50000],
    "Duration":['30days', '40Days','50Days','60Days']
}
index_label_row=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies,index=index_label_row)
technologies2={
    'Courses':["Spark","Java","Python","Go"],
    "Discount":[2000,3000,4000,5000]
}
index_label_row2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_label_row2)
print(df1)
print(df2)

df3=df1.join(df2, lsuffix="_left", rsuffix="_right",how="inner")
df3=df1.join(df2, lsuffix="_left", rsuffix="_right",how="right")
df3=df1.join(df2, lsuffix="_left", rsuffix="_right",how="outer")


print(df3)


df4=df1.join(df2.set_index('Courses'), how="inner",on ='Course')
print(df4)

df5=df1.set_index('Course').join(df2.set_index('Courses'), how="inner")
print(df5)


data=pd.read_csv("t20.csv")
print(data)