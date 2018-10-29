"""An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all 
the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, 
write a program that finds the sets of words that share the same characters that contain the most words in them."""

import itertools
from collections import defaultdict
f=open("C:/Users/..../unixdict.txt")
words=f.read().split("\n")
store=defaultdict(list)
def check_anagrams(a,b):
    return sorted(a)==sorted(b)
for a , b in itertools.combinations(words,2):
    if(check_anagrams(a,b)):
        store[a].append(b)
        
