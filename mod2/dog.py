class Dog:
    def __init__(self, name, birth_year, sound="woof,woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
    
    def bark(self,times):
        for _ in range(times):
            print(self.sound)
dog1 = Dog("Buddy", 2015)
dog2 = Dog("Max", 2018, "arf arf")
print(f"Dog1's name: {dog1.name}, Birth Year: {dog1.birth_year},{dog1.sound}")
print(f"Dog2's name: {dog2.name}, Birth Year: {dog2.birth_year}, Sound: {dog2.sound}")
dog1.bark(1)
dog2.bark(2) 

class Dog:
    created = 0
    def __init__(self, name, birth_year, sound="woof,woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound  
        Dog.created += 1
dog1 = Dog("Buddy", 2015)
dog2 = Dog("Max", 2018, "arf arf")
dog3 = Dog("Charlie", 2020, "bark bark")        
print(f"Total dogs created: {Dog.created}")