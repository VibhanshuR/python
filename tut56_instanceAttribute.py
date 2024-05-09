#instance attribute is different to all eg-salary,age of all employee
class employee:
      company="VRIndutries"
      salary=100

ankit=employee()
enimesh=employee()
print(ankit.company)
print(enimesh.company)
ankit.salary=300
enimesh.salary=400

print(ankit.salary)#instance have precedence over class attributes
print(enimesh.salary)