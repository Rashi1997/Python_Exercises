"""Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******"""

def histogram(lst):
    for l in lst:
        print(int(l)*'*')
lst=input("Enter the histogram lengths equally spaced ").split()
histogram(lst)
