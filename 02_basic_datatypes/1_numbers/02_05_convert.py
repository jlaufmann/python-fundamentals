'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

num_int = 6

#1
num_float = float(num_int)

#2
num_int = int(num_float)
# all the information after the decimal is lost

#3
ans_floor = num_float // num_int
ans_floor = num_int // num_float

#4
num1 = float(input('Please enter your first number: '))
num2 = float(input('Please enter your second number: '))
solution = num1 * num2
print(num1, 'x ', num2, '= ', solution)


