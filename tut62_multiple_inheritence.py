class freelancer:
    company="google"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

class Employee:
    company="google"
    empCode=100

class programmer(freelancer,Employee):
    name="rohit"

p=programmer()
print(p.company)
p.upgradeLevel()