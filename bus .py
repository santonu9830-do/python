# Parent class
class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity


# Child class
class Bus(Vehicle):
    def __init__(self, capacity, fare_per_passenger):
        super().__init__(capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self):
        return self.capacity * self.fare_per_passenger


# Example usage
bus = Bus(50, 20)  # 50 passengers, fare = 20 each
print("Total Fare:", bus.calculate_total_fare())