class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def me (self):
        print(f"{self.name} is {self.age} years old and is {self.gender}")

myPerson = Person("john",30,"male")
myPerson.me ()
myPerson = Person("lana",30,"female")
myPerson.me ()
    
