""" Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n."""

def filter_long_words(list_of_words,n):
    for w in list_of_words:
        if(len(w)>n):
            print(w)
            

list_of_words=input("Enter words ").split()
n=int(input("Enter threshold "))

filter_long_words(list_of_words,n)

    
