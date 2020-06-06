'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''

class Furniture:
    """ describes items of furniture found in a home """
    def __init__(self, name, function = 'general', colour = 'bland', room = 'cellar'):
        self.name = name
        self.function = function
        self.colour = colour
        self.room = room

    def __str__(self):
        return f"{self.name}, {self.function}, {self.colour}, {self.room}"

    def print(self):
        print(f"Item: {self.name}    Function: {self.function}    Colour: {self.colour}    In room: {self.room}")

# but when doing the __init__ if i set default values for those not given, if there is one value not given, how does the
# instance know which values have been given and which not?

class Person:
    """ describes different people """
    def __init__(self, name, country = 'unknown', colour = 'undefined', age = 0):
        self.name = name
        self.country = country
        self.colour = colour
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.country}, {self.colour}, {self.age}"

    def print(self):
        print(f"Name: {self.name}    Home Country: {self.country}    Skin colour: {self.colour}    Age: {self.age}")

class Animal:
    """ describes different animals """
    def __init__(self, name, colour = 'unknown', weight = 0, diet = 'unknown'):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.diet = diet

    def __str__(self):
        return f"{self.name}, {self.colour}, {self.weight}, {self.diet}"

    def print(self):
        print(f"Animal: {self.name}    Colour: {self.colour}    Weight: {self.weight}    Diet: {self.diet}")

    def __add__(self, other):
        """ enables the combined weight of two animals to be calculated """
        return self.weight + other.weight

# when would I define an instance/object like: self.size = weight ?

table = Furniture('Table', 'eating', 'brown', 'kitchen')
table.print()
print(table)

sofa = Furniture('Sofa', 'sitting', 'red', 'living room')
sofa.print()
print(sofa)

jim = Person('Jim', 'Australia', 'white', 38)
kerstin = Person('Kerstin', 'Germany', 'white', 36)
jim.print()
print(jim)
kerstin.print()
print(kerstin)

meerkat = Animal('Meerkat', 'grey', 3, 'herbivore')
dog = Animal('Dog', 'black', 7, 'carnivore')

meerkat.print()
print(meerkat)
dog.print()
print(dog)
print(f"Meerkat + Dog = {meerkat + dog}")


