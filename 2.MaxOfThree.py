"""Define a function max_of_three() that takes three numbers as arguments and returns the largest of them."""
def max_of_three(a,b,c):
    if(a>b and a>c):
        return a
    elif (b>a and b> c):
        return b
    elif (c>a and c> b):
        return c
a,b,c=input("Enter three numbers ").split()
maximum=max_of_three(a,b,c)
print (maximum)
