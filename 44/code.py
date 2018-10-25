
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
