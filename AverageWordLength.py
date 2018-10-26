import re
p=open("C:/Users/rasdhar/Desktop/Python Training/38/punctuations.txt")
punct=list(p.read())
#print(punct)
file=open("C:/Users/rasdhar/Desktop/Python Training/38/text.txt")
text=file.read()
words=re.split("\n| ",text)
frequency=list()
c=0
for word in words:
    for w in word:
        if w not in punct:
            c+=1
    frequency.append(c)
    c=0
avg=sum(frequency)/len(frequency)  
print(avg)
