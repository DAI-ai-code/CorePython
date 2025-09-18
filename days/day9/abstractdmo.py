from abc import ABC, abstractmethod


class Demo(ABC):

    @abstractmethod
    def demo_method(self):
        pass

class Demoed(Demo):

    @abstractmethod
    def demo_method(self):
        pass

class Demoder(Demoed):
    def demo_method(self):
        print('this ')

d = Demoder()
d.demo_method()