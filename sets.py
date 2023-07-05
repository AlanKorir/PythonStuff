#unorederd, mutable, no duplicates
myset = {1,2,3,1,2,3,4,5,6,6}
myset2 = set ([1,2,3,4,5,6,7,8])
myset3 = set('Hello')
myset4 = set() #empty set
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

#methods
# myset.add(1)
# myset.add(22)
# myset.add(31)
# myset.remove(22)
# myset.discard(311)
# myset2.clear()
# myset.pop()

#Looping
# for i in myset:
#     print (i)

# if 2 in myset:
#     print (True)

#union combines elements from 2 sets without duplication
u = odds.union(evens)

#intersection only takes elements found in both set
i = evens.intersection(primes)

#Difference returns all ements present in first set that are not in the second set
diff = myset.difference(evens)

#symmetric difference returns all elements that are in first and second sets but not those that are in both sets
diff2 = myset.symmetric_difference(evens)

#update returns a new set with elements from 2 sets
myset3.update(myset)

#intersection_update updates set by keeping elements found in both sets
myset.intersection_update(odds)

#differenc_update updates a set by removing elements found in the second set
myset2.difference_update(evens)

#symmetric_difference_update keeps elements found in first and second set but not those found in both 

myset2.symmetric_difference_update(evens)

#subset compares whether elements of 1st set are also in the second set

# print(myset.issubset(myset2))

#superset checks if all numbers in second set are in first set (opposite of subset)
# print(myset2.issuperset(myset))

#disjoint checks if same elements are not found in two sets

print(odds.isdisjoint(evens)) 

#frozenset is an immutable version of a set