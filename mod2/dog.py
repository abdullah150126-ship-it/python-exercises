def bark():
    print("Woof!")
    
def meow():
    print("Meow!")
    
from .dog import bark
from . cat import meow  

from animal import bark, meow
bark()
meow()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")      
        
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def meow(self):
        print(f"{self.name} says Meow!")  
        
from .dog import Dog
from .cat import Cat            