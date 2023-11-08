class Testing:
    num=100
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("i am constructor parent")
    def data(self):
        print("i am the method")

    def add(self):
        return self.a+self.b+self.num

print('Temp1')
# print('Temp2')
ob=Testing(4,5)
print(ob.add())
ob.data()

ob2=Testing(20,33)
print(ob2.add())

#Joins
a ="we are learning python in the training"
b="time for lunch"
print(a.join(b))


