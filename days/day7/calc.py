
class Calculator:

    def __init__(self):
        print('')

    def plus(self, *a):
        sum = 0
        for i in a:
            sum += i
        else:
            print(sum)

    def subtract(self, *a):
        sub = a[0]
        for i in a[1:]:
            sub -= i
        else:
            print(sub)

    def multiply(self, *a):
        res = 1
        for i in a:
            res *= i
        else:
            print(res)

    def divide(self,*a):
        res = a[0]
        for i in a[1:]:
            res /= i
        else:
            print(int(res))

calc = Calculator()
calc.subtract(1, 2, 3)
calc.multiply(1, 2, 3)
calc.divide(100, 2, 5)
