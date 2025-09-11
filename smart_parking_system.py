# Smart Parking System:
# • Create classes Vehicle, ParkingSpot, and ParkingLot.
# • Create multiple objects (vehicles, spots, parking lot).
# • Demonstrate object creation, attribute initialization, and method calls.
# • Make sensitive attributes private (e.g., license plate, owner name, spot status).
# • Provide getter/setter methods to access/update them safely.
# • Show that direct access fails but methods work.
# • Vehicle is the base class.
# • Derived classes:
# Bike (extra attribute: helmet_required)
# Car (extra attribute: seats)
# SUV (extra attribute: four_wheel_drive)
# Truck (extra attribute: max_load_capacity)
# • Each child class overrides display() to print its own details.
# • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
# • Iterate and call display() → each object responds differently.
# • Implement a calculate_parking_fee() method:
# Bike → ₹20/hour
# Car → ₹50/hour
# SUV → ₹70/hour
# Truck → ₹100/hour
# • Demonstrate runtime polymorphism by calling the method on different objects.
# • Create an abstract class/interface Payment (using abc module).
# • Define an abstract method process_payment(amount).
# • Create child classes:
# CashPayment
# CardPayment
# UPIPayment
# • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
# Task 1: Vehicle Classes
# Implement base and derived vehicle classes with encapsulation.
# Override display() and calculate_parking_fee().
# Task 2: ParkingSpot Class
# Implement ParkingSpot with size restrictions (S, M, L, XL).
# Methods: assign_vehicle(), remove_vehicle().
# Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
# Task 3: ParkingLot Class
# Store multiple parking spots.
# Methods:
# add_spot() → add new parking spots.
# show_spots() → display all spots and their status.
# park_vehicle(vehicle) → find suitable spot and park.
# unpark_vehicle(vehicle) → remove from spot and calculate fee.
# Task 4: Payment (Abstraction + Polymorphism)
# When un-parking a vehicle, calculate fee (based on hours).
# Ask user for payment method → process payment using appropriate child class.
# Task 5: Main Program
# Create a parking lot with mixed spots.
# Create multiple vehicle objects.
# Park/unpark vehicles.
# Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.
from abc import ABC

class Payment(ABC):
    @abstractmethod
    def process_payment(amount):
        pass
class CashPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")
class UPIPayment(Payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")


class Vehicle:
    def __init__(self,id,license_plate,owner_name):
        self.id=id
        self.__license_plate=license_plate
        self.__owner_name=owner_name
    def getlicenseplate():
        return self.license_plate
    def setlicenseplate(lp):
        self.license_plate=lp
    def getownername():
        return self.owner_name
    def setownername(on):
        self.owner_name=on
    def display():
        print("Vehicle details:\nLicense Plate:",self.license_plate,"\nOwner Name:",self.owner_name)
    def calculate_parking_fee():
        pass
class Bike(Vehicle):
    vehicle_type='Bike'
    def __init__(self,id,license_plate,owner_name,helmet_required):
        super().__init__(id,license_plate,owner_name)
        self.helmet_required=helmet_required
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nHelmet Required: ",self.helmet_required)
    def calculate_parking_fee(self,hr):
        20*hr
class Car(Vehicle):
    vehicle_type='Car'
    def __init__(self,id, license_plate, owner_name,seats):
        super().__init__(id,license_plate, owner_name)
        self.seats=seats
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nSeats: ",self.seats)
    def calculate_parking_fee(hr):
        return 50*hr
class SUV(Vehicle):
    vehicle_type='SUV'
    def __init__(self,id, license_plate, owner_name,four_wheel_drive):
        super().__init__(id,license_plate, owner_name)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nFour Wheel Drive:",self.four_wheel_drive)
    def calculate_parking_fee(hr):
        return 70*hr
class Truck(Vehicle):
    vehicle_type='Truck'
    def __init__(self,id, license_plate, owner_name,max_load_capacity):
        super().__init__(id,license_plate, owner_name)
        self.max_load_capacity=max_load_capacity
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_typeTruck,"\nMax Load Capactiy:",self.max_load_capacity)
    def calculate_parking_fee(hr):
        return 100*hr


class ParkingSpot:
    def __init__(self,spot,spot_size):
        self.__spot_size=spot_size
        self.spot=spot
    def assign_vehicle(spot_list,vehicle_size):
        for i in spot_list:


        # if v.vehicle_type=='Bike':
        #     self.spot_size='S+'
        # elif v.vehicle_type=='Car':
        #     self.spot_size='M+'
        # elif v.vehicle_type=='SUV':
        #     self.spot_size='L+'
        # elif v.vehicle_type=='Truck':
        #     self.spot_size='XL'
    def remove_vehicle():
        pass    #TO BE FILLED


class ParkingLot:
    def __init__(self,name):
        self.nameid
    def add_spot(l):
        l.append('E')
    def show_spots(l):
        s=1
        for i in l:
            print(f"Spot {s}:",end=" ")
            if i=='E':
                print("EmptySpot",end=" ")
            else:
                print("Occupied",end=" ")
    def park_vehicles(v,l):
        for i in l:
            if i=='E':
                if v.vehicle_type=='Bike'