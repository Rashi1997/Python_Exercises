"""A certain childrens game involves starting with a word in a particular category. Each participant in turn says a word, but that word 
must begin with the final letter of the previous word. Once a word has been given, it cannot be repeated. If an opponent cannot give a 
word in the category, they fall out of the game. For example, with "animals" as the category,
Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 English Pokemon names (extracted from Wikipedia's list of 
Pokemon) and generate the/a sequence with the highest possible number of Pokemon names where the subsequent name starts with the final 
letter of the preceding name. No Pokemon name is to be repeated.
audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""
import re
import itertools
from collections import defaultdict

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths    

loc="C:/Users/rasdhar/Desktop/Python Training/45/pokemon_names.txt"
with open(loc) as f:
    content=f.read()
f.close()
words=re.split("\n| ",content)
print (len(words))
graph=defaultdict(list)
for a,b in itertools.permutations(words,2):
    if(a[-1]==b[0]):
        graph[a].append(b)
#print (graph)
max_length=0;
for word in words:
    all_paths = DFS(graph, word)
    if all_paths:
        max_len   = max(len(p) for p in all_paths)
        if(max_len>max_length):
            max_length=max_len;
            max_paths = [p for p in all_paths if len(p) == max_len]

print (max_paths[1])
print (max_length)        
     
