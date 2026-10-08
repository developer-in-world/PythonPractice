"""
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    
"""

# the lame solution, we should use the logic and nested loops to solve this
# for i in range(5):
#     print("1 2 3 4 5")

# for i in range(5):
#     for j in range(1,6):
#         print(j, end=" ")
#     print()

"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

"""

# for i in range(1, 6):
#     for j in range(1,6):
#         print(i, end=" ")
#     print()

"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

"""

# for i in range(5, 0, -1):
#     for j in range(5):
#         print(i, end = " ")
#     print()

"""
*
* *
* * *
* * * *
* * * * *

"""

# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()    

""" 
* * * * *
* * * *
* * * 
* * 
*
"""

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""
# for i in range(1,6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print() changing the same as the dynamic get input from user and print

n = int(input("Enter the number to print: "))
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()