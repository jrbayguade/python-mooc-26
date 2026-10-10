mylist = [1, 2, 3, 4, 5]
newValue = ""

while newValue != "-1":
    index = int(input("Index: "))
    newValue = int(input("New value: "))

    mylist[index] = newValue

    print(mylist)