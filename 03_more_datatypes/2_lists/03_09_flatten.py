'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flattened_list = []

for lists in starting_list:
    for items in lists:
        flattened_list.append(items)

print(f"starting_list = {starting_list}")
print(f"flattened_list = {flattened_list}")
