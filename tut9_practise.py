job='''hi NAME
you are selected

on date=DATE
'''
name=input("enter your name\n")
date=input("enter date\n")
job=job.replace("NAME",name)
job=job.replace("DATE",date)
print("\n")
print(job)