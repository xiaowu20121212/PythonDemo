from collections import namedtuple

Person = namedtuple("Student", ["age", "name", "sex"])
s = Person(19, "xiaowu", "man")
print(s)
