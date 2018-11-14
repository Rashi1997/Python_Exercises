"""Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""
def sum_elements(lst):
    s=0
    for l in lst:
        s+=int(l)
    return s
def multiply(lst):
    m=1
    for l in lst:
        m*=int(l)
    return m
lst=input("Enter spaced out list elements ").split()
print(sum_elements(lst))
print(multiply(lst))
