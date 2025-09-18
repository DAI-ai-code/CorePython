# using neg index
a = [1,2,3,4,5]
a = a[::-1]
for i in a:
    print(i)

print("--------------")
a = [1,2,3,4,5]
for i in range(1,len(a)+1):
    print(a[-i])

print("--------------")
b = [1,2,3,4,5]
x = 0
y = len(b)-1
while x<y:
    b[x],b[y] = b[y],b[x]
    x+=1
    y-=1
for i in range(0,len(b)):
    print(b[i])

print("-------------------")
list = [i for i in range(0,101)]
l = [i for i in list if i%2!=0]
print(l)

print("-------------------------")
def isprime(a):
    for i in range (2,int(a**(1/2))+1):
        if a%i==0 :
            return False
    else:
        return True
l = [i for i in list if isprime(i) and i>=2]
print(l)

print("-------------------------")
a = [1, 2, 5, 6, 3, 6]
a.append(7)
print(a)
a.pop(-1)
print(a)

print("-------------------------")
a.remove(6)
print(a)
a.insert(len(a)+1,90)
print(a)

print("-------------------------")
c=a
b = a.copy()
a.pop()
print("a -> " + str(a))
print("b -> " + str(b))
print("c -> " + str(c))

print("-------------------------")
x=a+b
print(x)
a.extend(c)
print(a)
print("-------------------------")

a = [11, 52, 31, 4, 5, 4]
a.reverse()
# a.sort(reverse=True)
print(a)
