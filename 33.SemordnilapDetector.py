"""According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!"""


filename=input("Enter the name of the file ")
loc="C:/Users/rasdhar/Desktop/Python Training/40/"+filename+".txt"
file=open(loc)
words=file.read().split("\n")
for word in words:
    if word[::-1] in words and len(word)>4:
        print(word+" " +word[::-1])
