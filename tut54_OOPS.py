class railwayForm:
    formType="railwayForm"
    def printdata(self):
        print(f"name of person is {self.person}")
        print(f"name of person is {self.trainName}")

vrApplication=railwayForm()
vrApplication.person="rudra"
vrApplication.trainName="bullet train"
vrApplication.printdata()