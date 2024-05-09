with open('tut52.txt','r') as f:
    content=f.read()

content=content.replace("donkey","1@$%&*$%")

with open('tut52.txt','w') as f:
   f.write(content)
