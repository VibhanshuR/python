text=input("enter the text\n")

if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
else:
    spam=False

if(spam):
    print("this text is spam")
else:
    print("not a spam")
