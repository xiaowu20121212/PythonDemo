from random import randint
from collections import Counter
data = [randint(0, 20) for _x in range(30)]
#print(data)
#data = {_x: randint(0, 20) for _x in range(30)}
d = dict.fromkeys(data, 0)
#print(d)
for x in data:
    d[x] += 1
#print(d)

c = Counter(d)
print(c.most_common(3))