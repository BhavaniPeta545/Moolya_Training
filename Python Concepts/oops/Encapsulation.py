#wrpaiing the data
#data can be public,protected or private
#helps for preventing data modification
class Base:
    def __init__(self):
        self.a="company"
        self._b="moolya"
class Child(Base):
    def __init__(self):
        super().__init__()
        print(self._b)
ob=Child()
print(ob._b)


