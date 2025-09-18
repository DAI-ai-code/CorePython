# 1
# Swapping case without swapcase method
from itertools import count

s = 'AbcDEFghi'
b=''
for a in s:
    if a==a.upper():
        b+=a.lower()
    else:
        b+=a.upper()

print(b)

#2
s = "aaaabbcddd"
ss = ""
for i in s:
    if i not in ss:
        ss+=i
        ss+=str(s.count(i))
print(ss)

# 3
a = 'listen'
b = 'silent'

for i in a:
    if i not in b:
        print('Not anagrams')
        break
else:
    print('Anagram')

# 4
a = "abcdabcdabcd"
b= ""
for i in a:
    if i not in b:
        b+=i
print(b)

# 5
print('----------------------------')
s = "this is the ending of the world"
l = s.split(' ')
s = ''
a = len(l[0])
for i in l[1:]:
    if a < len(i):
        a = len(i)
        s = i
print(s)
print('----------------------------')
# 6
vowels = ['a', 'e', 'i', 'o', 'u']
s = "hello world"

l = ""
for i in vowels:
    if i in s:
        l += str(s.count(i)) +  " " + i + "\n"
print(l)

# 7
s = 'madam'
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

# 8
punc = [ ".", "'", "!", "?", ",", ":", ";", "-", "(",")", '"']
s = "Hello world! how's life"
a=''
for i in s:
    if i in punc:
        continue
    else:
        a += i
print(a)

# 9
s = 'Hello10how12are3you'
res = 0
for i in s:
    if i.isnumeric():
        res += int(i)
print(res)

# 10
s = "Hello my name is hello world program how are you hello world"
l = s.split(' ')
count = 0
wrd = ''

for i in l:
    if s.count(i)>count:
        count = s.count(i)
        wrd = i
else:
    print(wrd)

print('------------------------')

# 11
s = 'hello guys how is your family'
a = ''
l = s.split(' ')
ll = []

for i in l:
    ll.append(len(i))

ll.sort()
for i in ll:
    for j in l:
        if i == len(j):
            a = a + j + " "
            l.remove(j)

print(a)
print('------------------------')
# for i in l:

# 12
s = 'qwertyuiop'

for i in s:
    if s.count(i)>1:
        print("Not isogram")
        break
else:
    print("Isogram")

# 13
print('--------Q13-------------')
s = 'thisatest'
count = 0
ch = ''
b = ''
for i in s:
    if s.count(i) > count:
        count = s.count(i)
        ch = i
print('ch = ' + ch)
count = 0
for i in s:
    if i!=ch and s.count(i) > count:
        count = s.count(i)
        b = i
else:
    print(b)
print('------------------------')

# 14
s = "hello my name is himawari how are you huys"
l = s.split(' ')
s1 = ''
for i in range(0,len(l)):
    if l[i].startswith('h'):
        s1 += l[i] +" "
print(s1)

# 15
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
au = al.copy()
s = 'testing STRING !/.'
cl, cu, cs = 0, 0, 0
for i in s:
    if i in al:
        cl += 1
    elif i.lower() in au:
        cu += 1
    else:
        cs += 1
print(str(cl) + ' ' + str(cu) + ' ' + str(cs))