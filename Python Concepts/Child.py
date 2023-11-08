from oops.inheritance import Testing


class Child(Testing):
    num2=200

    def __init__(self):
        Testing.__init__(self,4,5)
        print("i am child constructor")

    def add2(self):
        return self.add()+self.num2

ob3=Child()
print(ob3.add2())
import datetime
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def age(name,birthyear):
        return name,datetime.date.today().year-birthyear
    @classmethod
    def age1(cls,name,birthyear):
        print("class method")
        return cls(name,datetime.date.today().year-birthyear)

    def display(self):
        print(self.name,self.age)
#
# sv=People.age("bhavani",1997)
# cm=People.age1("bhavani",1996)
# print(cm.age)
# print(sv.age)








