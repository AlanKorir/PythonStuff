mylist =  ["banana", "cherry", "apple"]
# print(mylist)

mylist2 = [5, True, "apple"]
# print(mylist2)

item = mylist[0:3]
# print(item)

def for_mylist():
    for i in mylist:
        print(i)

def if_mylist():
    item1 = input("Enter item to check in list: ")
    if item1 in mylist:
        print ("Yes!")
    else:
        print("no")
# for_mylist()
# if_mylist()
list_cpy = mylist[:] # select all elements and add them to a new list
mylist.append("lemon")
mylist.insert(1, "blueberry")
item3 = mylist.pop()
mylist.reverse()
mylist3 = [10,2,4,7,5,9]
# mylist3.sort()

b = [i*i for i in mylist3] #square elements in the list
print(mylist3)
print(b)







