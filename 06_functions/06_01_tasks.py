'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def div4or7(i: int):
    return (i%4 == 0 or i%7 == 0)

def div4and7(i: int):
    return(i%4 == 0 and i%7 == 0)

num_in = int(input("Enter an integer number between 1 and 1,000,000,000: "))

if num_in < 1 or num_in > 1000000000:
    print("Number is out of range!")
    quit()

new_div4or7 = div4or7(num_in)
new_div4and7 = div4and7(num_in)
print(f"The number is divisible by 4 or 7: {new_div4or7}")
print(f"The number is divisible by 4 and 7: {new_div4and7}")
