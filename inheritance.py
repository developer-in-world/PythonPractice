class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def eat(self) -> None:
        print("I am eating \n")
    
    def sleep(self) -> None:
        print("I am sleeping \n")

class Cat(Animal):
    def meow(self) -> None:
        print("Meow Meow Meow \n")

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def display(self) -> None:
        print(f"Name of the dog: {self.name} and age is {self.age}")
        print(f"Breed of the dog is {self.breed} \n")

    def bark(self) -> None:
        print("Bow Bow Bow \n")


d1 = Dog("Ani", 2, "Bull dog")
d1.bark()
d1.eat()
d1.sleep()
d1.display()
