from numexpr.necompiler import double

s1 = "aaabbcccdfgfff"

def removeduplicate(s1):
    s2 =''
    for i in s1:
        if i not in s2:
            s2+=i
    return s2
print(removeduplicate(s1))


def creator(l, n):
    l1 = []
    l2 = []
    c = 0
    while c<len(l):
        for i in range(0+c, n+c):
            l1.append(l[i])
        l2.append(l1)
        l1 = []
        c += n

    return l2
print(creator([1,2,3,4,5,6], 2))

#2
d = {"a":456, "b":679, "c":355, "d":53, "e":9809}
def getMax(d):
    mx = -1
    k = 0
    for i in d:
        if d.get(i) > mx:
            mx = d.get(i)
            k=i
    return k

print(getMax(d))
print("------------------")
# 3
def leap(y):
    if y%400==0:
        return True
    elif y%4==0 and y%100!=0:
        return True
    else:
        return False

print(leap(1900))
print("------------------")
s = 'The quick brown fox jumps over the lazy dog'
def pangram(s):
    s1 = s.lower()
    s1 = s.split()
    a = ''
    for i in s1:
        a += i
    print(s1)
    s1 = set(a)
    print(len(s1))

# string mathematical
# ss = '2 + 3 - 9 * 5 / 2'
"""
ll = ss.split(" ")
print(ll)
print(ll.index("/"))
def calc(s):
    l = s.split(" ")
    bodmas = ['/', '*', '+', '-']
    ans = 0
    while len(l) > 3:
        for i in range(0,len(bodmas)):
            a = l.index(i)
            if i == 0:
                ans = l[a-1] / l[a+1]
                l.pop("/")
            elif i == 1:
                ans = l[a - 1] * l[a + 1]
            elif i == 2:
                ans = l[a - 1] + l[a + 1]
            elif i == 3:
                ans = l[a - 1] - l[a + 1]
"""
print('---------String expression calculator----------------')
ss = '12 + 3 - 9 * 5 / 2 + 1'

def calc(ss):
    e = ss.split(' ')
    # print(e)
    bodmas = ['/', '*', '-', '+']

    for i in bodmas:
        while i in e:
            ans = 0
            a = e.index(i)
            if i == '/':
                ans = double(e[a - 1]) / double(e[a + 1])
            elif i == '*':
                ans = double(e[a - 1]) * double(e[a + 1])
            elif i == '-':
                ans = double(e[a - 1]) - double(e[a + 1])
            elif i == '+':
                ans = double(e[a - 1]) + double(e[a + 1])
            e[a-1] = ''
            e[a+1] = ''
            e[e.index(i)] = str(ans)
            s = ' '.join(e)
            e = s.split(' ')
            for j in e:
                if j=='':
                    e.remove(j)
            print(e)

    return double(e[0])
print(calc(ss))
print('------------------------------------')
