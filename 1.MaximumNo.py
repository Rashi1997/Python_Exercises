"""Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)"""

def maximum(a,b):
    if(a>b):
        return a
    elif (b>a):
        return b
    else:
        return 0

a=input("Enter the first number ")
b=input("Enter the second number ")
greater=maximum(a,b)
print("The greater no is: "+greater)
