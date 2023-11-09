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
    
    def vehicle_data(self):
        print(f"{self.typeof_vehicle} {self.year} {self.make} {self.model} {self.doors} {self.roof}")

def input_data():
    typeof_vehicle = input("Input the vehicle's type! Is it a car, truck, plane, boat, or broomstick?")
    year = input("What year is the vehicle?")
    make = input("What make is the vehicle?")
    model = input("What model is the vehicle?")
    doors = input("Is it a 2 or 4 door vehicle?")
    roof = input("Does the vehicle have a solid roof or a sun roof?")

    return typeof_vehicle, year, make, model, doors, roof
    
data_input = input_data()

thing = Automobile(*data_input)

thing.vehicle_data()
