f = open("http://www.puzzlers.org/pub/wordlists/unixdict.txt")
words=f.read().split("\n")
for word in words:
    if(len(word)>5 and word[::2] in words and word[1::2] in words):
        print(word+" makes "+ word[::2]+" and "+word[1::2])
