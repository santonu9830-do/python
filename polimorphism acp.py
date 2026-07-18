from abc import ABC, abstractmethod

# Abstract class
class Car(ABC):

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass


# BMW class
class BMW(Car):

    def speed(self):
        print("BMW runs at 250 km/h")

    def fuel_type(self):
        print("BMW uses Petrol")


# Ferrari class
class Ferrari(Car):

    def speed(self):
        print("Ferrari runs at 340 km/h")

    def fuel_type(self):
        print("Ferrari uses Petrol")


# Polymorphism
cars = [BMW(), Ferrari()]

for car in cars:
    car.speed()
    car.fuel_type()
    print()