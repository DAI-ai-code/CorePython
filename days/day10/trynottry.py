from days.day10.DemoException import DemoException


def skipper():
    a = int(input('Enter dividend:'))
    b = int(input('Enter divisor:'))
    c = a/b
    print('answer ', c,'hellu' )

    a = [1, 2, 3, 4]
    print(a[5])

    a = 5
    b = 0
    try :
        print(a/b)
    except ZeroDivisionError:
        print('zero division error')

    a = [1, 2, 3, 4]
    try :
        print(a[6])
    except IndexError:
        print('index error')

a = 1
if a==1:
    raise DemoException