arr = ["Hi", "Hello", "World", "Hehehe"]
for i in range(len(arr)):
    print(i, arr[i])

# the above is how we usually do when we want both index and value

# here we can use enumerate here which returns tuple with index and value and replaces the above
print("\n")
for i, name in enumerate(arr):
    print(i, name)
    #(index, value) we unpack it and display it, it does the same as above for loop for us
    