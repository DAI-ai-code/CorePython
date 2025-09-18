from itertools import count

d = {1:"Hello", 2:"World", "how":3, "2":"Word"}

d.setdefault(4,"yoyo")
print(d)
d.setdefault(1)
print(d)

s = 'hello world hello earth i am hello'
l = s.split(' ')
d = {}
for i in l:
    d[i] = s.count(i)
print(d)

t = (10,101,10,10,20,30,40,50)
print(t[0])

a = t.count(10)
print(a)
a = t.index(10)
print(a)

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d = dict()
for i in range(0, len(l1)):
    d[l1[i]] = l2[i]
print(d)

print("-----------------")

c = 0
for i in d:
    c+=1
print(c)
print("-----------------")
d = dict.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
s = 'hello world'
for i in d:
    d[i] = s.count(i)
print(d)
print("-----------------")

emp = {"a":49000, "b":50000, "c":78000, "d":89000, "e":20000}

for i in emp:
    if emp[i] < 50000:
        emp[i] += emp[i]/10
print(emp)
print("-----------------")

l = [('a', 1), ('b', 2), ('c', 3)]
d = {}
for i in l:
    d[i[0]] = i[1]
print(d)
print("-----------------")
d = {'A':'a', 'B':'b', 'C':'c'}
e = {}
l = list(d.keys())
for i in range (len(l)-1, -1, -1):
    e[l[i]] = d[l[i]]
print(e)

print("-----------------")
s = 'The quick brown fox jumps over the lazy dog'
s = s.lower()
s = s.split()
a = ''
for i in s:
    a+=i
print(s)
s1 = set(a)
print(len(s1))
print("-----------------")
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in al:
    if i not in a:
        print('not pangram')
        break
else:
    print('pangram')
print("-----------------")

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a','o':'b','p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O',
'C':'P', 'D':'Q','E':'R',
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# s1 = input()
s = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
enc = ''
dec = ''

for i in s:
    if i in key:
        dec += key[i]
    else:
        dec += i
print(dec)

text =''
for i in s:
    text += key.get(i,i)
print(text)

for i in dec:
    if i in key:
        enc += key[i]
    else:
        enc += i
print(enc)
print('-------------------')
l = ['abc', 'mno', 'aaa', 'pqr', 'mnop']
d = {}
n = 0

for i in l:
    d[i[0]] = []

print(d)
for i in d:
    for j in l:
        if j.startswith(i):
            d[i].append(j)
print(d)

print("-------------------")
d = {1:"A", 3:"B", 5:"C", 6:"A", 7:"B"}
v1 = list(d.keys())
k1 = list(d.values())
d2 = dict.fromkeys(d.values(), [])

for i in k1:
    d2[i] =[]

for i in v1:
    d2[d[i]].append(i)

print(d2)