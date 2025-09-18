l = [x for x in range(1, 11)]
print(l)

#
l = [x for x in range(1, 11)]
print(l)

#
l = [x for x in range(0,101) if x%2==0]
print(l)

#

l = [i for i in range (1,101) if (i<51 and i%2==0) or (i>50 and i%2!=0)]
print(l)

#
def fact(n):
    res = 1
    for i in range(n,0,-1):
        res*=i
    return res
l = [fact(i) for i in range(1,11)]
print(l)

#
def prime(n):
    for i in range(2,int(n)):
        if n%i==0:
            return False
    else:
        return True

l = [i for i in range(2, 101) if prime(i)]
print(l)

t = (i for i in range(1,11))
print(t)
print(next(t))

l = [i for i in range(1,11)]

g =  (i for i in l)

print(type(g))
print('--------------')
a = 0
def f(l):
    for i in l:
        print(next(f(l)))
        yield i

for i in g:
    print(next(g))

# print(type(f(l)))
print('-----------')

a = [( i for i in range(1, 10))]
b = (1, 2)
print(b)

print("----------------")
s = ["hello","world","how","are"]
vowels = ['a','e','i','o','u']

def aretwo(s):
    c = 0
    for i in vowels:
        for j in s:
            if j.count(i) > 0:
                c+=j.count(i)
    return c

lis = [i for i in s if aretwo(i)>1]
print(lis)
lis = [i for i in s if sum(1 for char in i if char in vowels) > 1]
print(lis)



