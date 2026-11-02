# # Bad example
# from abc import ABC, abstractmethod

# class BankAccount(ABC):

#     @abstractmethod
#     def deposit(self) -> None:
#         pass

#     @abstractmethod
#     def withdraw(self) -> None:
#         pass

# class SavingsAccount(BankAccount):

#     def deposit(self, amount:int) -> None:
#         print(f"Rs.{amount} has been deposited to your saving account.")

#     def withdraw(self, amount:int) -> None:
#         print(f"Rs.{amount} has been withdrawn from your saving account.")


# class FD(BankAccount):

#     def deposit(self, amount:int) -> None:
#             print(f"Rs.{amount} has been deposited to your saving account.")

#     def withdraw(self, amount:int) -> None:
#         raise ValueError("FD doesnt have this feature")


# Good example
from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__(self, amount:int) -> None:
        self.__balance = amount

    @abstractmethod
    def deposit(self) -> None:
        pass

class WithdrawableAccount(Account):
    
    def __init__(self, amount:int) -> None:
        super().__init__(amount)
        
    @abstractmethod
    def withdraw(self) -> None:
        pass

class SavingsAcc(WithdrawableAccount):

    def __init__(self, amount:int) -> None:
        super().__init__(amount)

    def deposit(self, amount:float):
        print(f"Amount deposited to your SavingsAccount rs.{amount}")

    def withdraw(self, amount:float):
        print(f"Amount withdrawn from your SavingsAccount rs.{amount}")

class FD(Account):
    
    def __init__(self, amount:int) -> None:
        super().__init__(amount)
        
    def deposit(self, amount:int):
        print(f"Amount deposited to your FixedAccount rs.{amount}")
        