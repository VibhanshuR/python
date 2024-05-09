#*****************this is also a single inheritence*********************

class Employee:
    Company="google"

    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):
     language="python"

     def bhasha(self):
        print(f"the language is {self.language}")
    
     def showDetails(self):
        print("this is an programmer")#preference of child class function

e=Employee()
#e.showDetails()
p=Programmer()#it inherite employee functions also 
print(p.Company)
p.bhasha()
p.showDetails()
