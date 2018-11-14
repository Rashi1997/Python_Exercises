"""Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True."""

def is_palindrome(string):
    if(string==string[::-1]):
        print("Yes")
    else:
        print("No")
string=input("Enter a string to check if pallindrome or not ")
is_palindrome(string)
