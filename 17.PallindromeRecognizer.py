""" Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir", or the
exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and
spacing are usually ignored."""


from string import punctuation

line=input("Enter the sentence ")


l=list()
for w in line:
    if w not in punctuation and w!=" ":
        l.append(w.lower())
if (l[::-1]==l):
    print("Yes")

