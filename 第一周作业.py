list1=[("zhangsan","17","110"),("lisi","18","120")]
while True:
    option=input("please use [delete|update|find|list|exit]:")
    if option == "delete":
        uname=input("Please enter the username you want to delete:")
        for i in list1:
            if uname == i[0]:
                list1.remove(i)
                print(uname,"is deleted!")
                break
        else:
            print("user is not exist!")
    if option == "update":
        uname=input('Please enter the data you want to update,(e.g:"name:ege:number"):')
        list2=uname.split(':')
        tuple1=(list2[0],list2[1],list2[2])
        for i in list1:
            if list2[0] == i[0]:
                list1.remove(i)
                list1.append(tuple1)
                print(list2[0],"update ok!")
                break
        else:
            print("user is not exist!")
    if option == "find":
        uname=input("Please enter the username you want to find:")
        for i in list1:
            if uname == i[0]:
                print(i[0],i[1],i[2])
                break
        else:
            print("user is not exist!")
    if option == "list":
        for i in list1:
            print(i[0],i[1],i[2])
    if option == "exit":
        print("bye")
        break
else:
    print("unknown option,please input again!")