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
        
