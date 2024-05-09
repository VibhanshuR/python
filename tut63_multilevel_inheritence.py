class person:
    country="india"

    def takebreath(self):
        print("i am breathing...")

class employee(person):
      company="VRIndustries"

      def getsalary(self):
        print(f"salary in {self.salary}")

      def takeBreath(self):
        print("i am an employeeso i am luckily breathing....")

class Programmer(employee):
    company="Fiverr"

    def getsalary(self):
        print("no salary to programmers")

    def takeBreath(self):
        super().takeBreath()#call inherited function
        print("i am an employeeso i am luckily breathing+++")

p=person()
p.takebreath()

e=employee()
#e.takeBreath()

p=Programmer()
p.takeBreath()