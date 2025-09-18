class Calculator:
    def add(self,a,b):
        # res = self.a
        # for i in self.b:
        #     res+=i
        return a + b

class AdvCal(Calculator):
    def add(self,a,b):
        ab = super().add(a, b)
        print(ab)
        return a*b

c = Calculator()
bb = c.add(6,8)
print(bb)

a = AdvCal()
bb = a.add(6,8)
print(bb)