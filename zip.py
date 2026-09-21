# Zip is python in built func to compare two or more list in python

a = [1,2,3,4,5]
b = ["Hi", "I", "Am", "Loving", "Python"]
c = [00, 11, 33, 44, 77]

for a, b, c, in zip(a,b,c):
    print(a, b, c) # it really useful function which I have learned when building another basic project which is under development

"""
Output for the code 

1 Hi 0
2 I 11
3 Am 33
4 Loving 44
5 Python 77

"""
