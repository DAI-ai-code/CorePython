#1
from CorePython.days.day6.comprehension import prime

l = ["apple","banana","apricot","ananas","amla","kiwi"]
f = [fruits.title() for fruits in l if fruits[0] == 'a']
print(f)
def isOdd(n):
    if n%2==0:
        return 'Even'
    else:
        return 'Odd'

d = {i:isOdd(i) for i in range(1, 11)}
print(d)

e = {i: 'Even' if i%2==0 else 'Odd' for i in range(1,11)}
print(e)

#8
names= ["abc","def","gfh","zyc"]
marks = {90,55,78,66}
op = zip(names,marks)
print(dict(op))
d = {}

# def add_to_dict(pair):
#     name, mark = pair
#     d[name] = mark

# op = map(add_to_dict,zip(names,marks))
# print(list(op))

d = {}
list(map(lambda a, b: d.update({a: b}), names, marks))
print(d)


d = {x:y for x,y in zip(names, marks)}
print(d)

d1 = {'a':1,'b':2,'c':3}
d2 = {}

# list(map(lambda a,b: d2.update({b:a}),d1.keys(),d1.values()))
a = tuple(map(lambda a,b: d2.update({b:a}),d1.keys(),d1.values()))
print(d2)
print(a)

#
l = [n**2 for n in range(2, 101) if prime(n)]
print(l)

#
s = 'aa12bb4c3d56'
l = [int(i) for i in s if i.isnumeric()]
print(l)