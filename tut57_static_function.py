class railwayForm:
    formType="railwayForm"
    def printdata(self):
        print(f"name of person is {self.person}")
        
    
    @staticmethod
    def greet():#no need to specify 'self' after static function
        print("good morning")

vrApplication=railwayForm()
vrApplication.person="rudra"
vrApplication.printdata()
vrApplication.greet()