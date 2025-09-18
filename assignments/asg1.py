"""

11. Remove duplicate elements from list
12. From given list of strings create another list of strings having 2 or more vowels
13. Find out total count of prime numbers and odd numbers in given tuple
14. Write a program to reverse given string.
15. Write a program to find if given string is pangram (it should have all characters from a to z)
16. Write a program to find if given string is anagram (it should have same charachters in any
rotation)
17. Change the case of each vowel in given string (e.g. hEllo should be converted to hellO ,
uppercase should be converted to lower and vice versa)
18. Reverse every word in given sentence. ("hello world how are you" should be converted to
"olleh dlrow woh era uoy")
19. In cryptography, a Caesar cipher is a very simple encryption techniques in which each
letter in the plain text is replaced by a letter some fixed number of positions down the
alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and
so on. The method is named after Julius Caesar, who used it to communicate with his
generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher
where the shift is 13. In Python, the key for ROT-13 may be represented by means of the
following dictionary:
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a','o':'b',
'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O',
'C':'P', 'D':'Q','E':'R',
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're
done, you will be able to read the following secret message:
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program will be able to both
encode and decode texts written in English.
"""
# 1. Write a program to swap 2 numbers
a, b = 10, 20
print('a = ' + str(a) + ' ' + 'b = ' + str(b))
a,b = b,a
print('a = ' + str(a) + ' ' + 'b = ' + str(b))

print('-----------------------------------------------------')

# 2. Write a program to calculate sum of digits of given three digit number
a = 312
d1 = a//100
d23 = a%100
d2 = d23//10
d3 = d23%10
s = d1 + d2 + d3
print('sum of digits = ' + str(s))

print('-----------------------------------------------------')

# 3. Find if given number is even or odd
a = 19
if a%2!=0:
    print('Number is odd')
else:
    print('Number is even')

# 4. Print grade of student based on his marks
grade = 67
if grade>70:
    print('DISTINCTION')
elif 70 >= grade > 60:
    print('FIRST CLASS')
elif 60 >= grade > 50:
    print('SECOND CLASS')
elif 50 >= grade > 40:
    print('PASS')
else:
    print('FAIL')

print('-----------------------------------------------------')

# 5. Calculate factorial of number
a = 5
p = 1
for i in range(1, a+1):
    p *= i
else:
    print('Factorial = ' + str(p))

print('-----------------------------------------------------')

# 6. Find if given number is prime or not
a = 8
for i in range(2, a):
    if a%i==0:
        print('Not Prime')
        break
else:
    print('Prime')

print('-----------------------------------------------------')

# 7. Write a program to reverse a list
l = [1, 2, 3, 4, 5]
a = []
for i in range(1, len(l)+1):
    a.append(l[-i])
else:
    print(a)

print('-----------------------------------------------------')

# 8. Write a program to add all even elements in list from 1 to 100
s = 0
for i in range(1, 101):
    if i%2==0:
        s += i
else:
    print('sum = ' + str(s))

print('-----------------------------------------------------')

# 9. Write a program to print all odd numbers from list
l = [1, 2, 3, 4, 5]
for i in l:
    if i%2!=0:
        print(str(i))

print('-----------------------------------------------------')

# 10. Write a program to create a list of prime numbers from 2 to 100
l = []
for i in range(2, 101):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        l.append(i)
else:
    print(l)












