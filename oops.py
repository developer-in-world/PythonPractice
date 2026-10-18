class Student:
    def __init__(self, name:str, age:int, gender:str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self) -> None:
        print(f"This is the self: {self}")
        print(self.name)
        print(self.age)
        print(self.gender)

s1 = Student("mg", 10, "M")
# print(s1)  # prints address <__main__.Student object at 0x7c19ff736a50>
s1.display()


"""
<__main__.Student object at 0x7d04442e2a50>
This is the self: <__main__.Student object at 0x7d04442e2a50>
mg
10
M

"""
