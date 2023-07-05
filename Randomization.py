import random

a = random.random()
b = random.uniform(1,10)
c = random.randint(1,10)
d = random.randrange(1,10)
e = random.normalvariate(0,1)
f = list("A,B,C,D,E")
g = random.choice(f)
h = random.choices(f)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)