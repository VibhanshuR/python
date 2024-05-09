sub1=int(input("enter your marks of sub1\n"))
sub2=int(input("enter your marks of sub1\n"))
sub3=int(input("enter your marks of sub1\n"))

if(sub1<33 or sub2<33 or sub3<33):
 print("you are fail in any of the subject")

elif(sub3+sub1+sub2)/3<40:
    print("you are fail as tottal percentage less then 40%") 
else:
    print("you are pass")    