'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

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


class Woodfurniture(Furniture):
    """ subclass of furniture, also includes type of wood it is constructed from """
    def __init__(self, name, function = 'general', colour = 'bland', room = 'cellar', wood = 'unknown'):
        super().__init__(name, function, colour, room)
        self.wood = wood

    def __str__(self):
        return f"{self.name}, {self.function}, {self.colour}, {self.room}, {self.wood}"

    def print(self):
        print(f"Item: {self.name}    Function: {self.function}    Colour: {self.colour}    In room: {self.room}    "
              f"Wood: {self.wood}")

# is there a way to inherit and then add to the print methods and the __str__ def?

# but when doing the __init__ if i set default values for those not given, if there is one value not given, how does the
# instance know which values have been given and which not?

class Person:
    """ describes different people """
    def __init__(self, name, country='unknown', colour='undefined', age=0):
        self.name = name
        self.country = country
        self.colour = colour
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.country}, {self.colour}, {self.age}"

    def print(self):
        print(f"Name: {self.name}    Home Country: {self.country}    Skin colour: {self.colour}    Age: {self.age}")


class Neanderthal(Person):
    """ sub class of person, has hair colour also """
    def __init__(self, name, country='unknown', colour='undefined', age=0, hair_col='brown'):
        super().__init__(name, country, colour, age)
        self.hair_col = hair_col

    def __str__(self):
        return f"{self.name}, {self.country}, {self.colour}, {self.age}, {self.hair_col}"

    def print(self):
        print(f"Name: {self.name}    Home Country: {self.country}    Skin colour: {self.colour}    Age: {self.age}    "
              f"Hair colour: {self.hair_col}")


class   Earlyone(Neanderthal):
    """ subclass of Neanderthal, has a motion characteristic """
    def __init__(self, name, country='unknown', colour='undefined', age=0, hair_col='brown', motion='stationary'):
        super().__init__(name, country, colour, age, hair_col)
        self.motion = motion

    def __str__(self):
        return f"{self.name}, {self.country}, {self.colour}, {self.age}, {self.hair_col}, {self.motion}"

    def print(self):
        print(f"Name: {self.name}    Home Country: {self.country}    Skin colour: {self.colour}    Age: {self.age}    "
              f"Hair colour: {self.hair_col}    Motion Method: {self.motion}")

'''
jim = Person('Jim', 'Australia', 'white', 38)
kerstin = Person('Kerstin', 'Germany', 'white', 36)
jim.print()
print(jim)
kerstin.print()
print(kerstin)

lucy = Neanderthal('Lucy', 'Ethiopia', 'brown', 21, 'light brown')
print(lucy)
lucy.print()


barry = Earlyone('Barry', 'Eritrea', 'black', 22, 'white', 'crawl')
print(barry)
barry.print()
'''

class Animal:
    """ describes different animals """
    def __init__(self, name, colour='unknown', weight=0, diet='unknown'):
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
