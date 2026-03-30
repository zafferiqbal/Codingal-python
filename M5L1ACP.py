class Dog:
    animal = "dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

dog1 = Dog("Labrador", "Black")
dog2 = Dog("German Shepherd", "Brown")

print("Dog 1:", dog1.animal, dog1.breed, dog1.colour)
print("Dog 2:", dog2.animal, dog2.breed, dog2.colour)