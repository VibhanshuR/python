#class attribute is same to all eg-company name for all employee
class employee:
      company="VRIndutries"

ankit=employee()
enimesh=employee()
print(ankit.company)
print(enimesh.company)

employee.company="youTube"

print(ankit.company)
print(enimesh.company)