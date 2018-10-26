number=4
name=input("Hello! What is your name?\n")
print("Well, "+name+", I am thinking of a number between 1 and 20.")
c=0
while(1):
    c+=1
    guess=input("Take a guess.\n")
    if(int(guess)<number):
        print("Your guess is too low.")
    elif(int(guess)>number):
        print("Your guess is too high.")
    else:
        print("Good job, "+name+"! You guessed my number in "+str(c)+" guesses!")
        break;
