#both getter and setter called decorators
class company:
    company="BharatGas"
    salary=5600
    salarybonus=500

    @property#this called getter
    def totalSalary(self):
        return self.salary+self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary
       

e=company()
print(e.totalSalary)#this function you need to execute in print function
e.totalSalary=5800
print(e.salary)
print(e.salarybonus)
      