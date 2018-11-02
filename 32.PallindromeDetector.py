"""Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome."""

from string import punctuation
filename=input("Enter the filename ")
loc="C:/Users/rasdhar/Desktop/Python Training/32/"+ filename+".txt"
file =open(loc)
lines=file.read().split("\n")
ls=list()
for line in lines:
    l=list()
    for w in line:
        if w not in punctuation and w!=" ":
            l.append(w.lower())
    ls.append(l)
    if (l[::-1]==l):
        print(line)
