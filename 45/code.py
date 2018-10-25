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
     
