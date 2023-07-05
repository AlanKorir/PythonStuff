# add10 = lambda new_number: new_number + 10
# input_number = int(input('Enter number: '))
# print('Your number is : ' + str(add10(input_number)))

# multiply2 = lambda x,y: x*y
# print(multiply2(2,7))
import math

points2D_list = [(1,2), (15,1), (5, -1), (10,4)]
points2D_sortby2nd = sorted(points2D_list, key=lambda x: x[1])
points2D_sortbysum = sorted(points2D_list, key=lambda x: x[0] + x[1])
points2D_sortbymult = sorted(points2D_list, key=lambda x: x[0] * x[1])

# print(points2D_list)
# print(points2D_sortby2nd)
# print(points2D_sortbysum)
# print(points2D_sortbymult)

#map functions - transforms elements in a list using a function

List1 = [1,2,3,4,5]
mapped = map(lambda x: x*math.factorial(x), List1)
mappedWithFor = [x*math.factorial(x) for x in List1]


# print(list(mapped))
# print(list(mappedWithFor))


List2 = [1,2,3,4,5,6]
filtered = filter(lambda x: x%2==0, List2)
print(list(filtered))

filtered2 = [x for x in List2 if x%2==0]
print(list(filtered2))

#reduce function
from functools import reduce
List3 = [1,2,3,4,5,6,7,8]
productList = reduce(lambda x,y: x*y, List3)
print(productList)




