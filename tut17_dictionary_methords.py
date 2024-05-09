myDict={
        "marks":[1,2,3],
        "hi":"how are you",
        "another" : {'vr':'footballer'},
        1:2
}

print(list(myDict.keys()))#prints keys of dictionary
print(myDict.values())
print(myDict.items())#prints all (key,values) of allitems of dictionary

print(myDict)
name={"name":"rudra",
     "hi":"i am fine"}
myDict.update(name)
print(myDict)

print(myDict.get("marks"))#does not throws error if wrong means not present in dictionary
                          #also
print(myDict["marks2"])   #but it can throws error if wrong                      