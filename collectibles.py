#collections: Counters, namedTuples, OrderdDicts, defaultdicts, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

# a = "aaaabbbccc"
# counter1 = Counter(a) #returns a dictionary
# print(counter1)
# print(counter1.items())
# print(counter1.values())
# print(counter1.keys())
# print(counter1.most_common(2)[0][1]) #returns a list with tuples
# print((list(counter1.elements())))

# Point = namedtuple(('Point'), 'x,y')
# pt = Point(1,-4)
# print(pt)
# print(pt.x, pt.y)

# d = defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d['c'])

d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.popleft()
d.extendleft([4,5,6])
d.rotate(1)
d.rotate(-1)
print(d)
