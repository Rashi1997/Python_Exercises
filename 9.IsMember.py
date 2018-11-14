"""Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)"""

def is_member(x,a):
    flag=0
    for i in a :
        if(int(x)==(i)):
            flag=1
            break
    if (flag==1):
        print("Yes")
    else:
        print("No")


lst=[2,4,2,3]
e=input("Enter an element ")
is_member(e,lst)
