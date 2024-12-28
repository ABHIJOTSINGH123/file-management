file=open("codingal.txt","r")
counter=0
context=file.read()
colist=context.split("\n")
for i in colist:
  if i:
    counter+=1
print("this is the no. of lines in this file ")
print(counter)