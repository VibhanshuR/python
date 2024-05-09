class details:

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("hi harry")
    
    def printdata(self):
        print(f"name of person is {self.name}")
        print(f"name of person is {self.salary}")
        print(f"name of person is {self.subunit}")
        
    
    @staticmethod
    def greet():#no need to specify 'self' after static function
        print("good morning")

person1=details("harry",100,"youtube")
person1.printdata()