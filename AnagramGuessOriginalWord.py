import random
file=open("C:/Users/rasdhar/Desktop/Python Training/40/unixdict.txt")
words=file.read().split("\n")
file.close()
word=random.choice(words)
print(word)
lst=list(word)
random.shuffle(lst)
anagram=''.join(lst)
print(anagram)
while(1):
    guess=input("Guess: ")
    if(sorted(guess)==sorted(anagram)):
        print("Correct!!")
        break;
    
