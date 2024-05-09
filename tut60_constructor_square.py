class square:

    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"the area of square is {self.num**2}")

    def cube(self):
        print(f"the cube of square is {self.num**3}")


vinayak=square(4)
vinayak.square()
vinayak.cube()