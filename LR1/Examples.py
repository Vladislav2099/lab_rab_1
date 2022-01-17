a = {1, 2, 0, 1, 3, 2}
print(a)


a = set('data')
print(a)


a = {'set', 'str', 'dict', 'list'}
b = ','.join(a)
print(b)
print(type(b))

a = {('a', 2), ('b', 4)}
b = dict(a)
print(b)
print(type(b))

a = {1, 2, 0, 1, 3, 2}
b = list(a)
print(b)
print(type(b))

a = {0, 1, 12, 'b', 'ab', 3, 2, 'a'}
print(a)

a = {0, 1, 12, 3, 2}
print(a)

a = {0, 1, 12, 3, 2}
b = list(a)
print(b)

a = {0, 1, 2, 3, 4}
b = {3, 2, 1}
print(a.issubset(b))

a = {0, 1, 2, 3, 4}
b = {3, 2, 1}
print(a.issuperset(b))

a = frozenset({"hello", "world"})
print(a)

a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
c = a.union(b)
print(c)

a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
a.update(b)
print(a)

a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
c = a.intersection(b)
print(c)

a = {0, 1, 2, 3}
b = {4, 3, 2, 1}
c = a.difference(b)
print(c)

a = {0, 1, 2, 3}
print(2 in a)


a = {0, 1, 2, 3}
print(2 not in a)


for a in {0, 1, 2}:
    print(a)

a = {0, 1, 2, 3}
print(len(a))

a = {0, 1, 2, 3}
a.add(4)
print(a)

a = {0, 1, 2, 3}
a.remove(3)
print(a)

a = {0, 1, 2, 3}
a.clear()
print(a)

a = {i for i in [1, 2, 0, 1, 3, 2]}
print(a)
