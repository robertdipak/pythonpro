user=["user1", "user2"]
pwd= ["123","456"]
uname=input("Enter The Username")

if uname in user:
    print("User Findout successfully")
    
position= ''
r=False
for i in range(len(user)):
    if uname==user[i]:
        position=i;
        r=True
        break
print("Position of user is ",position, ".")
log=False
if(r):
    passwd=input("Enter The Password")
    if passwd==pwd[position]:
       
        print("\t",user[position], " has successfully logged \t",end="")
        log=True
    else:
        print("\tPassword mitch mass with username=",user[position],end="")
else:
    print("User has not findout",end="\n")

product=["product1", "product2"]
rate=[200, 300]
qty=[12,13]

prod_pos=-1
prod_find=False

if(log):
    i=0
    while(i<len(product)):
        print(product[i], end="\t")
        print(rate[i], end="\t")
        print(qty[i],end="\n")
        i=i+1
    addproduct=[]
    addqty=[]
    addrate=[]
    while True:
        ch=input("Want to add to cart product 'yes'")
        if ch=="yes":
            prod_nm=input("Enter The Product Name ")
            for i in range(len(product)):
                if(prod_nm==product[i]):
                    prod_pos=i;
                    prod_find=True
                    break

            if prod_find:
                
                q= int(input("Enter The Quantity"))
                if(q<=qty[prod_pos]):
                    
                    add_product_position=-1
                    add_product_find=False
                    for i in range(len(addproduct)):
                        if prod_nm==addproduct[i]:
                            add_product_find=True
                            add_product_position=i
                            print(add_product_position)
                            break
                    print(add_product_position)
                    if add_product_find:
                        print(addqty[0])
                        addqty[0]=addqty.pop(0)+q
                        addrate[add_product_position]=rate[prod_pos]

                        
                    else:
                        print(rate[prod_pos])
                        addproduct.append(prod_nm)
                        addqty.append(q)
                        addrate.append(rate[prod_pos])
                        qty[prod_pos]=qty[prod_pos]-q
                
                else:
                    print("Quantity of ", prod_nm, " is not available")
            else:
                print("Product has not findout", end="\n")
        else:
            break   
    print("*********** add to cart ************")
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
    print("*********** add to cart ************")
    rm=input(" product  remove 'yes'")
    if rm =='yes':
        p=input("enter product name")
        
        for i in range(len(addproduct)):
            if p==addproduct[i]:
                addproduct.pop(i)
                addqty.pop(i)
                addrate.pop(i)
                break
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")             

    totalpay=0
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
        totalpay+=addqty[i]*addrate[i]
        print("total payment to pay is ",totalpay)



