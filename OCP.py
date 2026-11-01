# Open Closed Principle
# Bad example

# class PaymentProcessor:
#     def pay(self, payment_method:str, amount:float) -> None:
#         if payment_method == "UPI":
#             print(f"Payment using UPI has started for amount Rs.{amount}")
#         else:
#             print("payment declined ma")

# if I needed to add new for paypal, I adding new if else in the existing method pay, that is bad modifying the existing code, that is prohibited
# p = PaymentProcessor()
# p.pay("UPI",1000)


# Good example

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self, amount:int) -> None:
        pass

class UPIPayment(PaymentMethod):

    def pay(self, amount:int) -> None:
        print(f"Payment through UPI for amount rs.{amount}")


class NETPayment(PaymentMethod):

    def pay(self, amount: int) -> None:
        print(f"Payment through NET for amount rs.{amount}")


class DebitCardPayment(PaymentMethod):

    def pay(self, amount: int) -> None:
        print(f"Payment through Debitcard for amount rs.{amount}")


class PaymentProcessor:
    def paymentProcess(self, payment_method:PaymentMethod, amount:int) -> None:
        payment_method.pay(amount)


upi = UPIPayment()
dc = DebitCardPayment()
net = NETPayment()

payment = PaymentProcessor()
payment.paymentProcess(upi, 1000)
payment.paymentProcess(dc, 1000)
payment.paymentProcess(net, 1000)

