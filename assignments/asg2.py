
def add_numbers(*n):
    sum = 0
    for i in n:
        sum += i
    return sum
print(add_numbers(1, 2, 3))
print('-----------------------------------------------------')

def perform_action(mylist, num):
    l = []
    for i in range(len(mylist)/num):
        l.append([])
    for i in range(len(l)):
        l[i]