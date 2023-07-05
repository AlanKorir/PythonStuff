#only immutable object can be used. (Cannot be changed after creation)

mydict = {'name': 'Max', 'age': 28, 'city':'Nakuru'}
mydict2 = dict(name='John', age=30, city='Dubai')
mydict3 = {3: 9, 6: 36, 9: 81}
mytuple = (8,7)
mydict4 = {mytuple : 15}
#adding items
# value = mydict['name'] 
# mydict['email'] = 'max@xyz.com'

# deleting items
# del mydict['name']
# mydict.pop('city')
# mydict.popitem()

#conditionals and exceptions
# if 'name' in mydict:
#     print(mydict['name'])

# try:
#     print(mydict['age'])
# except:
#     print('Error')

# looping 
# for key in mydict:
#     print (key, '\n')
# for value in mydict.values():
#     print(value, '\n')
# for key,value in mydict.items():
#     print(key,value, '\n')

#making dict copies
# mydictcopy = mydict  #modifies also the original dict
# mydictcopy2 = mydict.copy() #doesnt modify original dict
# mydictcopy3 = dict(mydict) #doesnt modify original dict
# mydictcopy['area'] = 'arable'
# mydictcopy2['box'] = 200

#merging dicts
# mydict.update(mydict2) #overwrites original dict with second dict values if keys are same

print(mydict4)