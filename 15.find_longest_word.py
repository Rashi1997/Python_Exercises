""" Write a function find_longest_word() that takes a list of words and returns the length of the longest one."""

def find_longest_word(list_of_words):
    list_of_lengths=list()
    for w in list_of_words:
        list_of_lengths.append(len(w))
    return max(list_of_lengths)
list_of_words=input("Enter words ").split()
print(find_longest_word(list_of_words))
