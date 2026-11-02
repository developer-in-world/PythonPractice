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