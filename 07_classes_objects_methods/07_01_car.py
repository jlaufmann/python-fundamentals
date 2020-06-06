'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    """ represents a car with model, year of manufacture and max-speed """
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"Your car is a {self.model} built in {self.year} with max-speed {self.max_speed} kph."

    def accelerate(self):
        """ increases the max_speed of car by 5 """
        self.max_speed += 5

toyota = Car('Corolla', 1984, 60)
ford = Car('Falcon', 1978, 80)
print(toyota)
print(ford)
ford.accelerate()
print(ford)
