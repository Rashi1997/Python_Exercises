"""Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: 
http://inventwithpython.com) This is how it should work when run in a terminal:

>>> import guess_number
Hello! What is your name?
Torbjörn
Well, Torbjörn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjörn! You guessed my number in 3 guesses!"""

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
