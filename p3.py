def login(userlist,passlist):
    print(userlist ,"\t")
    print(passlist, "\n")
    name= input("Enter User name")
    p=int(input("Enter the password"))
    for i in range(len(userlist)):
        if(name==userlist[i] and p==passlist[i]):
            return True
        
    return False


user=["user1", "admin"]
pass1=[12345,12346]
count=0
while True:
    if(login(user, pass1)):
        print("User login Successful")
    else:
        print("Failed to logining")
        count+=1
        if(count>=3):
            break


# if(login("admin", 12345)):
#     print("login ")
# else:
#     print("not login")

# login("deepak", 123)