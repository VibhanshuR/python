def percentage(marks):
    #return (marks[1]+marks[2]+marks[3]+marks[4])/4
    p=sum(marks)/4#sum[marks] is predefined function in python
    #p=(marks[0]+marks[1]+marks[2]+marks[3])/4
    return p

marks1=[34,67,98,78]
percentage1=percentage(marks1)


marks2=[56,99,43,8]
percentage2=percentage(marks2)

print(percentage1,percentage2)