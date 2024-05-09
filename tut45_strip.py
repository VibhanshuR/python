def remove_and_split(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()

this="      i am vr   "
print(remove_and_split(this,"vr"))