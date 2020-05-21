'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
from math import pi
radius = 3.14
height = 5.0

volume = pi * radius**2 * height
surface_area = (2 * pi * radius**2) + (2 * pi * radius * height)

print('radius of cylinder = ', str(radius))
print('height of cylinder = ', str(height))
print('volume = ', str(volume))
print('surface area = ', str(surface_area))

# volume = 154.874
# surface_area = 160.5957
