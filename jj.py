class Vecale():
    def init(self,name,speed,mile):
        self.name=name
        self.speed=speed
        self.mile=mile
    def Seating(self,capacity):
        print(f"The seating capacity of {self.name}")


v = Vecale("jjj",180,50)

v.Seating()

