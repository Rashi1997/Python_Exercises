"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon"."""
vowels=['a','e','i','o','u']

def translate(string):
    s1=''
    for s in string:
        if(s not in  vowels and s!=' '):
            s1+=s
            s1+='o'
            s1+=s
        else:
            s1+=s
    return s1
string=input("Enter a string to encode ")
print(translate(string))
