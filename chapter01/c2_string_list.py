# NoneType
# four numeric types: int, float, complex, bool
# four sequence types: str, list, tuple, range
# one mapping type: dict
# two set types: set, frozenset
# function, generator, type


# string methods
# s.capitalize(), s.count(substring, [start, end]), s.explandtabs([tabsize])
# s.endswith(substring, [start, end]), s.find(substring, [start, end])
# s.isalnum(), s.isalpha(), s.isdigit(), s.split([separator], [maxsplit])
# s.join(t), s.lower(), s.raplace(old, new[maxreplace]), s.swapcase()
# s.startswith(substring, [start, end]), s.strip([characters]), s.lstrip([characters])


greet = 'hello world'
print("2nd character is", greet[1])
print("character from 0th to 8th index are ", greet[0:8])
print(greet[0:8:2])
print(greet[0::2])
print(greet[1::2])
# example to understand traversing a string through loop
print("example to understand traversing a string through loop")
for i in enumerate(greet[0:5]):
    print(i)


# examples for list
x = 1
y = 2
z = 3
list1 = [x, y, z]
list2 = list1
list2[1] = 4
print("list 1 items are", list1)


items = [["rice", 2.4, 8], ["flour", 1.9, 5], ["corn", 4.7, 6]]
for item in items:
    print("Product: %s price: %.2f Quality: %i" % (item[0], item[1], item[2]))


# list comprehensions
def f1(x):
    return x * 2


def f2(x):
    return x * 4


lst = []
for i in range(16):
    lst.append(f1(f2(i)))
print(lst)
print([f1(x) for x in range(64) if x in [f2(j) for j in range(16)]])
