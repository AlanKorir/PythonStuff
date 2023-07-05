#Syntax errors - occur when parser detects a syntatically incorrect statement
#Exceptions - errors raised when syntax is correct but incorrect data

#raising exceptions
x = 54321
b = 111

def Exception1():
        raise Exception('Wrong PIN')


assert (x!=b), 'x is equal!'

try:
    a = 5 / 1
    c = 30 + a
except ZeroDivisionError:
    print('Dont do it')
except TypeError:
    print('You aint got no type!')
else:
    print('go ahead')
finally:
    print('cleanup')

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value too high!')
    if x < 100:
        raise ValueTooSmallError('Value too Small!', x)
try:
    test_value(50)
except ValueTooHighError as e:
    print (e)
except ValueTooSmallError as e:
    print (e.message, e.value)

