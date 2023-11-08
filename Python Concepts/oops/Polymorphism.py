class Language:
    def speak(self):
        print("many people speak many languages")

class Hyderanad(Language):
    def speak(self):
        print("Hydrabad people speak hindi")

class Banglore(Language):
    pass

ob=Banglore()
ob.speak()
obj=Hyderanad()
obj.speak()
