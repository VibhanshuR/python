f=open('tut47_file.txt')
#data=f.read(6)#read 5 character
data=f.readline()#read 1st line
print(data)
data=f.readline()#read 2nd line
print(data)
f.close()