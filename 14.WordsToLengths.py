""" Write a program that maps a list of words into a list of integers representing the lengths of the correponding words."""

list_of_words=input("Enter words ").split()
list_of_lengths=list()
for w in list_of_words:
    list_of_lengths.append(len(w))

print(list_of_lengths)
