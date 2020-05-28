'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

my_dict = {}

for num in range(1,11):
    my_dict[num] = num**2

print(f"dictionary: {my_dict}")
