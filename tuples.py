mytuple = ("Max", 28, "Boston")
mytuple2 = (["Max", 28, "Boston"])
mytuple3 = ('a','a','c','g','r','c')
mytuple4 = (1,2,3,4,5,6,7,8,9,10)

i1, *i2, i3 = mytuple4  # the *packages all elements between
name,age,city = mytuple
b = mytuple4[::-2] # reverse even
item = mytuple[-3]
# mytuple[0] = "Tim" tuples are immmutable

# for i in mytuple2:    iterating in tuples
#     print(i)

# if "Max" in mytuple2:
#     print("Yes!")  

mylist = list(mytuple)


import sys
mylist2 = [0,1,2,"hello", True]
mytuple5 = (0,1,2, "hello", True)

# print(sys.getsizeof(mylist2), "bytes")
# print(sys.getsizeof(mytuple5), "bytes") # a tuple take up less space than a list

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=10000000))









