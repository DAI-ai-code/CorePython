
ss= ['ABCCBA','PALINDROME', 'RACECAR']

def filter_palindrome(s):
    if s[::1]==s[::-1]:
        return True
    else:
        return False

a = filter(filter_palindrome,ss)
print(list(a))

def squaremaker(n):
    if n%2 != 0:
        return n*n
    else:
        return n

b = [1, 2, 3, 4, 5]
a = map(squaremaker,b)
print(list(a))


def finddupe(s):
    for i in s:
        if s.count(i)>1:
            return True
    return False

ss = ["Hello", "world", "byeee","bot"]
a = filter(finddupe,ss)
print(list(a))

def swapper(s):
    if ord(s[0]) > 93:
        return s.swapcase()
    return s

ss = ["Hello", "worLD", "byEEe","bOT"]
a = map(swapper,ss)
print(list(a))
