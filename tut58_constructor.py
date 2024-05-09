class railwayForm:

    def __init__(self):
       print("hi harry")
    
    def printdata(self):
        print(f"name of person is {self.person}")
        
    
    @staticmethod
    def greet():#no need to specify 'self' after static function
        print("good morning")

harry=railwayForm()#'hi harry' will automatically call without calling init function