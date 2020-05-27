'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

num_string = input("Enter 10 numbers separated by commas: ")
nums = num_string.split(',')
if len(nums) != 10:
    print("Numbers entered incorrectly, or not 10 numbers")
    quit()

numbers = list(map(float, nums)) #converted to floats rather than ints for more flexibility

num_max = max(numbers)
print(f"Your Numbers: {numbers}")
print(f"Largest Number: {num_max}")

num_prod = 1
for num in numbers:
    num_prod *= num

print(f"Product of all your numbers: {num_prod}")
