#product, permutations, #combinations, accumulator, groupby, infinite

#product
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b, repeat=2)

#permutations(order matters i.e 6,5 != 5,6)
from itertools import permutations
c = [5,6,7,8]
perm = permutations(c, 2)
# print('Perms: ', list(perm))

#combinations(order does not matter i.e 1,2 = 2,1)
from itertools import combinations, combinations_with_replacement
d = [5,6,7,8]
comb = combinations(d, 2)
comb2 = combinations_with_replacement(d, 2)
# print('Combs: ', list(comb))
# print('Combs2: ', list(comb2))

#accumulate
from itertools import accumulate
import operator
e = [1,2,5,4,2]
acc = accumulate(e)
multiply_acc = accumulate(e, func=operator.mul)
max_e = accumulate(e, func=max)
# print(e)
# print(list(acc))
# print(list(multiply_acc))
# print(list(max_e))

#groupby
from itertools import groupby

# def smallerThanThree(x):
#     return x < 3

f = [1,2,3,4,6,7,8]
# group1 = groupby(f, key=smallerThanThree) #f taken as arg for given function
# for key, value in group1:
#     print(key, list(value))


# group1 = groupby(f, key=lambda x: x<3) #declares and calls code immediately
# for key, value in group1:
#     print(key, list(value))

#example of a lambda function
# fun1 = lambda s: s*3
# print(fun1(6))
persons = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 45},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 35},
    {'name': 'Eve', 'age': 45}
]

#groups by age !note it groups sequentially
# group2 = groupby(persons, key=lambda x: x['age'])
# for key, value in group2:
#     print(key, list(value))

#infinite iterators
from itertools import count,cycle, repeat

#count makes an infinite counting loop
# for i in count(10): #arg is the start value
#     print(i)
#     if i == 20:
#         break

#cycle infinitely cycles thru an iterable(e.g list)
# g = [1,2,3]
# for i in cycle(g):
#     print(i)
#     if i == 3:
#         break

#repeat infinitely repeats the arg

# for i in repeat(a):
#     print(i)