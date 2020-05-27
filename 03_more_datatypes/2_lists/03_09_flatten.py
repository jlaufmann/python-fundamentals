'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
# get list from input:
print('In the format: [[1, 2, 3, 4], [5, 6], [7, 8, 9]]')
string_in = input("Enter your list: ")

string_in1 = string_in.replace(" ","") # removing whitespace from string
#print(f"string without white space: {string_in1}")

list_in = string_in1.strip('][').split('],[') # splitting string into list
#print(f"string split into list: {list_in}")

starting_list = []
for sublist in list_in: # splitting sub-strings into items
    starting_list.append(sublist.split(','))
    # print(sublist)

'''
If we assume the list contains only integers, the code between the hashed lines can be executed.
If list contains only floats, it could be slightly modified.
If list contains other itmes the code between the hashed lines should be commented out.
'''
#####################################################################
starting_list_ints = []
for sublist in starting_list:
    sublist2 = []
    for ints in sublist:
        sublist2.append(int(ints))
    starting_list_ints.append(sublist2)
starting_list = starting_list_ints
#####################################################################
print(f"starting_list = {starting_list}")

# example starting list:
# starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flattened_list = []

for lists in starting_list:
    for items in lists:
        flattened_list.append(items)

print(f"flattened_list = {flattened_list}")
