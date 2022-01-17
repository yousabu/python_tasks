class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        
    def Seating_Capacity(self,capacity):
        return f"The Seating Capacity of {self.name} is {capacity} Passengers"
    
class Bus(Vehicle):
    def Seating_Capacity(self,capacity=50):
        return super().Seating_capacity(capacity=50)


b = Bus("bus",180,50)
print(b.Seating_Capacity())