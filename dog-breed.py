class dog:
    animal = "Dog"
    def __init__(self, b, c):
        self.breed = b
        self.colour = c

d1 = dog("german sheperd","brown")
d2 = dog("pug","white")

print("animal:", d1.animal, "breed:", d1.breed, "colour:", d1.colour)
print("animal:", d2.animal, "breed:", d2.breed, "colour:", d2.colour)
