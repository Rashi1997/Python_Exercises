"""Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file)."""
f=open("C:/Users/rasdhar/Desktop/Python Training/37/text_file.txt")
lines=f.read().split("\n")
f.close()
f_output=open("C:/Users/rasdhar/Desktop/Python Training/37/list_text_file.txt",'w')
i=1
for line in lines:
    f_output.write(str(i)+". "+line+"\n")
    i+=1
f_output.close()
