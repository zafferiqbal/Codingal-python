class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def fare(self):
        base_fare = super().fare()
        return base_fare + (0.1 * base_fare)


bus = Bus()
print("Total Bus Fare:", bus.fare())