"""Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen."""
from string import punctuation
from collections import Counter
import string

def char_freq_table(content):
    char=list()
    alpha=list(string.ascii_lowercase)
    for w in content:
        if w.lower() in  alpha:
            char.append(w.lower())
    frequency=sorted(Counter(char).items())
    return frequency
filename=input("Enter your filename ")
loc="C:/Users/rasdhar/Desktop/Python Training/34/"+filename+".txt"
file=open(loc)
content=file.read()
frequency=char_freq_table(content)
file.close()
from prettytable import PrettyTable
    
x = PrettyTable()

x.field_names = ["Word", "Frequency"]
for k,v in frequency:
    x.add_row([k, v])


print(x)
