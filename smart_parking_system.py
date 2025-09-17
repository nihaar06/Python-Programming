"""
Smart Parking System
--------------------
This program models a smart parking system demonstrating core OOP concepts:
encapsulation, inheritance, polymorphism, and abstraction.

Classes:
- Vehicle (base class) with derived classes Bike, Car, SUV, Truck.
- ParkingSpot represents individual parking spots with size restrictions.
- ParkingLot manages multiple spots and parking operations.
- Payment (abstract class) with implementations CashPayment, CardPayment, UPIPayment.

Features:
- Private sensitive attributes with getters/setters for safe access.
- Vehicle polymorphism in display and parking fee calculation.
- Spot size compatibility enforced during parking.
- Abstracted payment processing options.
"""
from abc import ABC,abstractmethod


class Payment(ABC):
    """Abstract base class for payment methods."""
    @abstractmethod
    def process_payment(self,amount):
        pass

class CashPayment(Payment):
    def process_payment(self,amount):
        print(f"Paid Rs.{amount} in cash")

class CardPayment(Payment):
    def process_payment(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")

class UPIPayment(Payment):
    def process_payment(self,amount):
        print(f"Paid Rs.{amount} using UPI")


class Vehicle:
    """Base vehicle class with private license plate and owner name."""
    def __init__(self,id,license_plate,owner_name):
        self.id=id
        self.__license_plate=license_plate
        self.__owner_name=owner_name
    def get_license_plate(self):
        return self.__license_plate
    def set_license_plate(self,lp):
        self.__license_plate=lp
    def get_owner_name(self):
        return self.__owner_name
    def set_owner_name(self,on):
        self.__owner_name=on
    def display(self):
        """Display basic vehicle info."""
        print("Vehicle details:\nLicense Plate:",self.__license_plate,"\nOwner Name:",self.__owner_name)
    def calculate_parking_fee(self):
        return None
    
class Bike(Vehicle):
    vehicle_type='Bike'
    size='S'
    def __init__(self,id,license_plate,owner_name,helmet_required):
        super().__init__(id,license_plate,owner_name)
        self.helmet_required=helmet_required
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nHelmet Required: ",self.helmet_required)
    def calculate_parking_fee(self,hr):
        return 20*hr
class Car(Vehicle):
    vehicle_type='Car'
    size='M'
    def __init__(self,id, license_plate, owner_name,seats):
        super().__init__(id,license_plate, owner_name)
        self.seats=seats
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nSeats: ",self.seats)
    def calculate_parking_fee(self,hr):
        return 50*hr
class SUV(Vehicle):
    vehicle_type='SUV'
    size='L'
    def __init__(self,id, license_plate, owner_name,four_wheel_drive):
        super().__init__(id,license_plate, owner_name)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nFour Wheel Drive:",self.four_wheel_drive)
    def calculate_parking_fee(self,hr):
        return 70*hr
class Truck(Vehicle):
    vehicle_type='Truck'
    size='XL'
    def __init__(self,id, license_plate, owner_name,max_load_capacity):
        super().__init__(id,license_plate, owner_name)
        self.max_load_capacity=max_load_capacity
    def display(self):
        super().display()
        print("Vehicle Type:",self.vehicle_type,"\nMax Load Capactiy:",self.max_load_capacity)
    def calculate_parking_fee(self,hr):
        return 100*hr


class ParkingSpot:
    """Represents a parking spot with size and occupancy status."""
    def __init__(self,spot_size,status,vehicle):
        self.__spot_size=spot_size
        self.__status=status
        self.__vehicle=vehicle
    def get_status(self):
        return self.__status
    def set_status(self,st):
        self.__status=st
    def get_spot_size(self):
        return self.__spot_size
    def set_spot_size(self,ss):
        self.__spot_size=ss
    def get_vehicle(self):
        return self.__vehicle
    def set_vehicle(self,v):
        self.__vehicle=v
    def assign_vehicle(self,vehicle):
        if self.get_status()=='Empty':
            if vehicle.size=='S':
                self.set_status("Occupied")
                self.set_vehicle(vehicle)
                return True
            elif vehicle.size=='M' and (self.__spot_size=='M' or self.__spot_size=='L' or self.__spot_size=='XL'):
                self.set_status("Occupied")
                self.set_vehicle(vehicle)
                return True
            elif vehicle.size=='L' and (self.__spot_size=='L' or self.__spot_size=='XL'):
                self.set_status("Occupied")
                self.set_vehicle(vehicle)
                return True
            elif vehicle.size=='XL' and (self.__spot_size=='XL'):           
                self.set_status("Occupied")
                self.set_vehicle(vehicle)
                return True
            else:
                return False
        else:
            return False
    def remove_vehicle(self):
        temp=self.get_vehicle()
        self.set_status("Empty")
        self.set_vehicle(None)
        return temp


class ParkingLot:
    """Manages multiple parking spots and operations."""
    def __init__(self,name):
        self.name=name
        self.spots=list()
    def add_spot(self,spot):
        self.spots.append(spot)
    def show_spots(self):
        j=0
        for i in self.spots:
            print("Spot number:",j+1)
            print("Spot size:",i.get_spot_size())
            print("Status:",i.get_status())
            if(i.get_status()=='Occupied'):
                print("Details:\n")
                i.get_vehicle().display()
            j+=1
    def park_vehicle(self,vehicle):
        for i in self.spots:
            if i.get_status()=='Empty':
                if i.assign_vehicle(vehicle)==True:
                    return True
        return False
    def unpark_vehicle(self,vehicle,hours,payment_method):
        for i in self.spots:
            if i.get_vehicle() is not None and i.get_vehicle().get_license_plate()==vehicle.get_license_plate():
                i.remove_vehicle()
                fare=vehicle.calculate_parking_fee(hours)
                payment_method.process_payment(fare)
                return fare
        return None
    
    
def main():
    lot = ParkingLot("City Center Lot")
    # Add mixed spots
    for size in ["S", "M", "L", "XL"]:
        lot.add_spot(ParkingSpot(size, "Empty", None))

    # Create vehicles
    vehicles = [
        Bike(1, "KA01AB1234", "Alice", True),
        Car(2, "KA02CD5678", "Bob", 4),
        SUV(3, "KA03EF9012", "Charlie", True),
        Truck(4, "KA04GH3456", "Diana", 5000)
    ]

    # Park vehicles
    for v in vehicles:
        lot.park_vehicle(v)

    lot.show_spots()

    # Unpark with payment
    payments = [CashPayment(), CardPayment(), UPIPayment(), CashPayment()]
    hours = 2
    for v, p in zip(vehicles, payments):
        fare = lot.unpark_vehicle(v, hours, p)
        print(f"Unparked {v.vehicle_type} - Fee: Rs.{fare}")

if __name__ == "__main__":
    main()
