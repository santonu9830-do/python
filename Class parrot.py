class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot("Blu", 10)
woody = parrot("Woody", 15)

print("Blu is a {}".format(blu.species))
print("Woody is a {}".format(woody.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woody.name, woody.age))