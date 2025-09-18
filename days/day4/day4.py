print('testing')
e = {'emp':[1,2,3,4]}

#Functions


# even or odd
def iseven(a):
    if(a%2==0):
        return "Even"
    else:
        return "Odd"

print(iseven(5))
def fct(a):
    r=1
    for i in range(a,0,-1):
        r*=i
    return r

ab=fct(5)
print(ab)

# add 0 to n
def adder(n):
    s = 0
    for i in range(0, n+1):
        s += i
    return s
print(adder(5))

#prime
def isprime(n):
    sq = int(n**(1/2))
    for i in range(2,sq+1):
        if n%i == 0:
            # print("Not prime")
            return False
    else:
        # print("Prime")
        return True

print('Is it prime? Ans: ' + str(isprime(55)))

def summer(a, b):
    s = 0
    for i in range(a, b+1):
        s += i
    else:
        print(s)
summer(1, 10)

def primer(n):
    l = []
    for i in range(2, n+1):
        if isprime(i):
            l.append(i)
    else:
        print(l)

primer(100)



