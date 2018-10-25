
with open("C:/Users/..../Salutations.txt") as sal:
    salutations=sal.read().split("\n")
sal.close()
loc="C:/Users/..../sentence.txt"
with open(loc) as f:
    para=f.read()
f.close()
words=para.split(" ")
#print (salutations)
result=open("C:/Users/..../output.txt",'w')
for word, next_word in zip(words[:-1], words[1:]):
    if(word in salutations):
        result.write(word+" ")
    elif(word[-1]=="." and word not in salutations and next_word[0].isupper()):
        result.write(word + "\n")
    elif(word[-1]=="?" and next_word[0].isupper()):
        result.write(word + "\n")
    else:
        result.write(word+" ")
result.write(words[-1])
result.close()   
