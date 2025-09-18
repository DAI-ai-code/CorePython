list1 = list()
for i in range(1,101,2):
    list1.append(i)
print(list1)
print("-------------------------")

list2 = []
for i in range(2,101):
    for j in range(2, int(i**(1/2)+1)):
        if i%j==0:

            break
    else:
        list2.append(i)
print(list2)
print("-------------------------")
list3 = [11,1,1,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,7,7,7,7]
list4 = []
list3.sort()
inLoop = False
a=0
while a<len(list3):
    while a<len(list3)-1 and list3[a] == list3[a+1]:
        a+=1
        inLoop = True
    if inLoop:
        list4.append(list3[a])
    inLoop = False
    a+=1
print("-> " + str(list4))
print("-------------------------")

a = []
l = list3.copy()
# for i in range(0)
print("-------------------------")
l = [1,2,3]
k = [2,3,4]
j = []
for i in range(0,len(k)):
    j.append(l[i]+k[i])
print(j)
print("-------------------------")
l1 = l.copy()
l2 = [1, 2]

for i in range(0, len(l2)):
    l1[i] += l2[i]

print(l1)
print('-------------------------')
list3 = [11,1,1,2,2,3,3,3,3,4,4,4,4,4,5,5,5,6,7,7,7,7]
list4 = []
list3.sort()
inLoop = False
a=0
while a<len(list3):
    while a<len(list3)-1 and list3[a] == list3[a+1]:
        a+=1
        inLoop = True
    list4.append(list3[a])
    a+=1
print("-> " + str(list4))
print("------------STRINGS LAB-------------")
s = "hello world"
a = ""
for i in range(len(s)-1, -1, -1):
    a += s[i]
print(a)
b = ''
for i in range(1, len(s)+1):
    b += s[-i]
print(b)

list = [10,20,30]
res=0
for i in list:
    res+=i
um = "{:.2f}".format(res)
print(um)

s="Hello World"
print(s.find('l'))
print(s.count('l'))
print(s.endswith('rld'))
print(' '.isspace())
print('10 12'.isnumeric())
print('10 12'.strip()[0].isnumeric())
print('i am. my is.\n i am'.capitalize())
print("--------------------------------")
s = 'hELLO worLD'
a = s[0].upper() + s[1:]
print(a)

s = "Hello,world,how,are,you"
print(s.split(","))
l = s.split(',')
print(','.join(l))
print(' '.join('hello'))
print('x'.join(l).split('x'))

s = "hello world how are you"
l = s.split(" ")
ss = []
for i in l:
    ss.append(i[::-1])
ss = " ".join(ss)
print(ss)
s = "testing try"
print("".join(reversed(s)))
# Swapping case without swapcase method
s = 'AbcDEFghi'
b=''
for a in s:
    if a==a.upper():
        b+=a.lower()
    else:
        b+=a.upper()

print(b)
print("----------------------------------------")

s = """This is my class 
       This is python class
       There are sixty students in
       python class"""
l =[]
s = s.split('\n')
for i in s:
    i.strip()
print(s)
s.split(" ")
s.remove('\n')
s.remove('')

def findcount(wrd):
    return s.count(wrd)

for i in s:
    if i!= '':
        l.append(findcount(i))
print(s)
print(l)