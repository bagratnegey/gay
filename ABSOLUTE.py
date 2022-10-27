from collections import UserDict
class Bag(UserDict):
    def __add__(self,other):
        self.data.update(other)
        return self
    def __sub__(self,other):
        for key in other:
            if key in other:
                self.data.pop.key()
                return self
d1=Bag