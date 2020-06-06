'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self, name, colour, mass, system):
        """ represents a planet with colour, mass and the system it belongs to """
        self.name = name
        self.colour = colour
        self.mass = mass
        self.system = system

    def __str__(self):
        return f"{self.name} is a {self.colour} planet weighing {self.mass} tonnes in the {self.system}"

    def grow(self):
        """ increases the mass of the planet """
        self.mass *= 1.1

    def shrink(self):
        """ reduces the mass of the planet """
        self.mass *= 0.8

mars = Planet('Mars', 'red', 5000, 'solar system')
earth = Planet('Earth', 'blue', 10000, 'solar system')
scribeldee = Planet('Scribeldee', 'purple', 90000, 'scribeldum system')

print(mars)
mars.grow()
print(mars)
mars.shrink()
print(mars)

