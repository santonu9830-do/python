class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "dogesh ka bhai")
dog2 = Dog("dogesh", "kalu")

print("Species:", Dog.species)
print("Dog 1:", dog1.name, "-", dog1.breed)
print("Dog 2:", dog2.name, "-", dog2.breed)
