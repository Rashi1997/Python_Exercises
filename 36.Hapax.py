"""A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization."""
import re
from collections import Counter

loc="C:/Users/rasdhar/Desktop/Python Training/38/punctuations.txt"
file=open(loc)
punct=file.read()
file.close()
loc2="C:/Users/rasdhar/Desktop/Python Training/36/text.txt"
loc1="C:/Users/rasdhar/Desktop/Python Training/36/text_cleaned.txt"
file1=open(loc2)
content=file1.read()
file1.close()
file1=open(loc1,'w')
words=re.split("\n| ",content)
for word in words:
    for w in word:
        if w not in punct:
            file1.write(w.lower())
    file1.write(" ")
file1.close()
file1=open(loc1)
words=file1.read().split(" ")
file1.close()    
frequency = Counter(words)
for k,v in frequency.items():
    if v==1:
        print(k)
    
