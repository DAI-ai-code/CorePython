# 1.Write a function to add n numbers
def add_numbers(*n):
    sum = 0
    for i in n:
        sum += i
    return sum
print(add_numbers(1, 2, 3))

print('-----------------------------------------------------')

# 2. Create new list after every nth element from mylist
def perform_action(mylist, num):
    l2 = []
    n1 = 0
    n2 = num
    for i in range(int(len(mylist)/num) + 1 ):
        l1 = [i for i in mylist[n1:n2]]
        n1 += num
        n2 += num
        l2.append(l1)
    else:
        print(l2)

perform_action([1, 2, 3, 4, 5, 6, 7, 8], 3)

print('-----------------------------------------------------')

# 3. Take two string lists (namelist, surnamelist) as parameters for a function and final output should
# be like [name1 surname1, name2 surname2.....]
name_list = ['Rakesh', 'Mohit', 'Manoj']
surname_list = ['Sharma', 'Kumar', 'Shekhawat']

def name_surname(namelist, surnamelist):
    l = []
    for i in range(len(namelist)):
        l.append(namelist[i] + ' ' + surnamelist[i])
    return l

print(name_surname(name_list, surname_list))

print('-----------------------------------------------------')

# Write a function to seperate elements from given iterable (list, tuple, set) and create 3 different
# lists for oddnumber, even numbers and prime numbers

def separator(iterable):

    def is_prime(n):
        for j in range(2, int(n**0.5) + 1):
            if n%j == 0:
                return False
        else:
            return True

    prime_list = []
    odd_list = []
    even_list = []
    for i in iterable:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
        if is_prime(i) and i!=1:
            prime_list.append(i)

    print(f'odd numbers = {odd_list}, even numbers = {even_list}, prime numbers = {prime_list}')

separator([1, 2, 3, 4, 5, 6, 7])
separator((1, 2, 3, 4, 5, 6, 7))
separator({1, 2, 3, 4, 5, 6, 7})


