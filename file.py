file_read=open('codingal.txt','r')
print(file_read.read())
file_read.close()
file_write=open('codingal.txt','w')
print("file in write mode")
file_write.write("Hi! I am Penguin and I am 1 yr old")
file_write.close()
file_read=open('codingal.txt','r')
print(file_read.read())
file_read.close()
file_append=open('codingal.txt','a')
print("file in append mode")
file_append.write("\n I am Penguin and I am 1 yr old")
file_append.write("Hi! I am Penguin and I am 1 yr old")
file_append.close()
file_read=open('codingal.txt','r')
print(file_read.read())
file_read.close()