"""Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops"""

def overlapping(a,b):
    flag=0
    for i in a:
        if(i in b):
            flag=1
            break
    if(flag==1):
        print("True")
    else:
        print("False")
lst1=input("Enter equally spaced list 1 elements ").split()
lst2=input("Enter equally spaced list 2 elements ").split()
overlapping(lst1,lst2)
