'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

int1, int2 = list(map(int, input("Enter two integer numbers separated by a comma: ").split(',')))

if int2 >= int1:
    intend = int2+1     # we want to include int2 in the list
    step = 1            # +ve step needed to produce list
else:
    intend = int2-1
    step = -1           # -ve step needed to produce list

# intsum = sum(range(int1, intend, step))   # would be more efficient :)

intsum = 0
for i in range(int1, intend, step):
    intsum += i

print(f"The sum is: {intsum}")
