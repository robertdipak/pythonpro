import csv
import json
# data=[]
header=['user','age']
with open("data1.csv", "r") as readcsv:
    reader=csv.reader(readcsv)
    flag=False
    header = []
    for i in reader:
        if(flag== False):
            header = i
            flag = True
        # print(i)
        # print("Company Name :"+ i[0]+"\n")

with open("newfile.csv", "w") as writecsv:
    # writer= csv.DictWriter(writecsv, fieldnames=header)
    writer= csv.writer(writecsv) 
    # writer.writeheader()
    data=[]
    with open("data1.csv", "r") as readcsv:
        reader = csv.reader(readcsv)
        # listdatat=list(reader)
        # print(listdatat[1])
        match = input("Enter the Car Name")
        count =0
        for i in reader:
            # print(list(reader).index(list(reader)[0]))
            if count==0:
                data.append(i)
                count=count+1
            if match == i[0]:
                data.append(i)
                print("match")
    writer.writerows(data)
    print(data)



            # print("Company Name :"+ i[0]+"\n")
            

