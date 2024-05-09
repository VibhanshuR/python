class Employee:
    company="VRindustries"
    salary=100
    location="india"

    #def changeSalary(self,sal):
        #self.salary=sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)