"""Your task in this exercise is as follows:
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that 
order), none of which mis-nest.
Examples:
   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK"""

string=input("Enter a string")
stack=list()
for s in string:
    if(s==']' and not stack):
        stack.append(s)
        break;
    elif(s=='['):
        stack.append(s)
    elif(s==']'):
        e=stack.pop()
print(stack)
if not stack:
    print ("OK")
else:
    print ("NOT OK")
