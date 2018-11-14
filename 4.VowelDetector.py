"""Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""
a=input("Enter a character ")
vowels=['a','e','i','o','u']
while(len(a)!=1):
    a=input("Enter a character of length 1 ")
    if(len(a)==1):
        if(a in vowels):
            print("True")
        else:
            print("False")
