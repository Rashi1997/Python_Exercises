hidden="tiger"
print("[][][][][]")
c=0
while(c!=5):
    word=input("Enter a guess: ")
    print("Clue: ",end='')
    c=0
    for a, b in zip(word,hidden):
        if(a==b):
            c+=1
            print("["+a+"]", end='')
        elif(a in hidden):
            print("("+a+")", end='')
        else:
            print(a, end=''),
    print("\n")
