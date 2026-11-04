def add(n1:int, n2:int, n3:int) -> int:
    return n1+n2+n3

ans = add(1,2,3)
print(ans)

def can_vote(age:int):
    if age >= 18:
        return True
    else:
        return False
    # it directly exits function and stops other flows which are coded below the return

ans = can_vote(20)
print(f"Answer for this {ans}")
# This shows that the return statement is useful for computing the steps and returning back too compute further

def square_number(num:int) -> float:
    return num ** 2

print(square_number(4))

def min_of_three(num1:int, num2:int, num3:int) -> int:
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else:
        return num3

print(min_of_three(-1,1,0))

def absolute_value(num:int) -> int:

    if num >= 0:
        return num
    else:
        return num * -1

print(absolute_value(-100)) 