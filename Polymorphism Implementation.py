class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
         print(f"I am Cat named {self.name} my age {self.age}")
         
    def make_sound(self):
        print("Meow")
        
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
         print(f"I am Dog named {self.name} my age {self.age}")
         
    def make_sound(self):
        print("bark")
        
Cat1=Cat("mini",2.5)
Dog1=Dog("G.O.A.T",10)
for animal in(Cat1,Dog1):
    animal.make_sound()
    animal.info()