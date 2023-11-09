#Lea Nicole Kerr
#M03 Lab/case study
#This app/program uses classes to take user input and display data on a vehicle

class Vehicle(): #superclass
    def __init__(self, typeof_vehicle):
          self.typeof_vehicle = typeof_vehicle


class Automobile(Vehicle): #class/subclass that inherits vehicle's attributes
     def __init__(self, typeof_vehicle, year, make, model, doors, roof):
        super().__init__(typeof_vehicle) 
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
     def car_data(self):
        self.typeof_vehicle = "Car"
        self.year = input("What year is the car?")
        self.make = input("What make?")
        self.model = input("What model?")
        self.doors = input("Is it a 2 or 4 door car?")
        self.roof = input("Does the car have a solid roof or a sun roof?")

typeof_vehicle = ""
year = ""
make = ""
model = ""
doors = ""
roof = ""

car_stuff = Automobile(typeof_vehicle, year, make, model, doors, roof)
car_stuff.car_data()

print("Type of vehicle is a:", car_stuff.typeof_vehicle)
print("Car year is:", car_stuff.year)
print("Make is:", car_stuff.make)
print("Car model is:", car_stuff.model)
print("Car doors:", car_stuff.doors)
print("Car roof is:", car_stuff.roof)

