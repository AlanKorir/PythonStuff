import json

myDeets = {'name': 'Max', 'age': 28, 'city':'Nakuru'}

#serialization - conveting python obj to json data format
myDeetsjson = json.dumps(myDeets, indent=4, sort_keys=True)

with open('theFam2.json', 'w') as file:
    json.dump(myDeets, file, indent=4)


#deserialization - converting from json to py
person2 = json.loads(myDeetsjson)
print(person2)

##using a class method with serialization
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable') 
user1json = json.dumps(user1, default=encode_user)

##serialization using built in JSONEncoder method
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

user2Json = UserEncoder().encode(user1)
print(user2Json)

##custom decoder function for above 

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct



user3 = json.loads(user2Json, object_hook=decode_user)
print(user3.age)