with open('tut49_file.txt','r') as f:
   a=f.read()
with open('tut49_file.txt','w') as f:
   a=f.write("me and only")
   print(a)
#no need to close in with 