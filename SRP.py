# Single Responsibility Principle (SRP)

# Bad Example
class User:
    
    def __init__(self, name:str, age:int, email:str) -> None:
        self.__name = name
        self.__age = age
        self.__email = email
    
    def get_user_info(self) -> None:
        print(f"Details of the user: ")
        print(f"Name: {self.__name}")
        print(f"age: {self.__age}")
        print(f"Email address: {self.__email}")
    
    def is_adult(self) -> bool:
        return self.__age >= 18
    
    def save_to_database(self) -> None:
        print(f"{self.__name} is been saved to the database.")
    
    def delete_from_database(self) -> None:
        print("User has been deleted from the database.")
        
        
# Good Example
""" We create this , the below class has each one purpose alone, not like
the above one class is able to manage user and his database in the db.
Which is bad and violates the S in the solid."""

class UserG:
    
    def __init__(self, name:str, age:int, email:str) -> None:
            self.__name = name
            self.__age = age
            self.__email = email
        
    def get_user_info(self) -> None:
        print(f"Details of the user: ")
        print(f"Name: {self.__name}")
        print(f"age: {self.__age}")
        print(f"Email address: {self.__email}")
        
    def is_adult(self) -> bool:
        return self.__age >= 18
    
class UserRepo:
    def __init__(self, userObject:UserG) -> None:
        self.__userobj = userObject
        
    def save_to_database(self) -> None:
        print(f"{self.__name} is been saved to the database.")
        
    def delete_from_database(self) -> None:
        print("User has been deleted from the database.")
    
    
    