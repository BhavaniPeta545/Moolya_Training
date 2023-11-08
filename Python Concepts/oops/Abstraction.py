#create method where dont have implemention
#abs class/mrthod cant executed
from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def speak(self):
        pass    #implementation happens in child class

class Parrot(Animal):
    def speak(self):
        print("parrot is speaking")

# ob=Parrot("cuckoo")
# ob.speak()
obj=Animal("dob")
obj.speak()

