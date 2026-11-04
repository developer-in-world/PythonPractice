def greet() -> None:
    print("Good morning")
    print("Good afternoon")
    print("Good night")
    
def odd_or_even(number:int) -> bool:
    return number%2 == 0

def print_factors(number:int) -> None:
    for i in range(1, number+1):
        if number%i == 0:
            print(i, end=" ")
    print()


print_factors(22)
print_factors(100)


def addition(a:int,b:int,c:int) -> None: #parameters defined inside the function
    print(f"Total = {a+b+c}")


addition(1,1,1) # Arguements passed into the function


def rectangle(length:int, breadth:int) -> None:
    print(f"Area of the rectangle = {length*breadth}")

rectangle(22,10)

def find_max(num1:int, num2:int, num3:int) -> None:
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3 and num2 > num1:
        print(num2)
    else:
        print(num3)


find_max(11,2,3)



def discount_price(price:int, discount_percentage:float) -> float:
    discount_price = price * discount_percentage
    final_price = price - discount_price
    return f"Discounted price = {final_price}"

print(discount_price(1000, 0.5))
