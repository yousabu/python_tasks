"""
#1
class Vehicle:
    def init(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    def init(self,name,max_speed,mileage):
        super().init(name,max_speed,mileage)
        print(f"Vehicle Name: {self.name} || Max_Speed: {self.max_speed} || Mileage: {self.mileage}")

b1=Bus("bus",180,50)

"""


#2
class Vehicle:
    def init(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def Seating_Capacity(self,capacity):
        print(f"The Seating Capacity of {self.name} is {capacity} Passengers")
    
class Bus(Vehicle):
    def init(self,name,max_speed,mileage):
        super().init(name,max_speed,mileage)
    def Seating_Capacity(self,capacity=50):
        print(f"The Seating Capacity of {self.name} is {capacity} Passengers")

Bus("bus",180,50)
Bus.Seating_Capacity()



"""
#3
class Vehicle:
    def init(self,name,max_speed,mileage,capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def Fare(self):
        return self.capacity*100
               
class Bus(Vehicle):
    def init(self,name,max_speed,mileage):
        super().init(name,max_speed,mileage,capacity=50)
    def Fare(self):
        return self.capacity*100+(0.1*self.capacity*100)
    
b3=Bus("bus",180,50)
print("Total Bus Free is :",b3.Fare())
"""

