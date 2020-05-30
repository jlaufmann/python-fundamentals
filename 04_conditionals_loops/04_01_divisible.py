'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

my_num = float(input("Enter a number between 1 and 1,000,000,000: "))

if my_num < 1 or my_num > 1000000000:
    print("Your number is out of range!")
    quit()

if my_num % 3 == 0:
    print("Your number is divisible by 3")
    my_num = int(my_num)
    print(f"{my_num} / 3 = {my_num // 3}")
else:
    print("Your number is not divisible by 3")
    print(f"{my_num} / 3 = {my_num / 3}")
