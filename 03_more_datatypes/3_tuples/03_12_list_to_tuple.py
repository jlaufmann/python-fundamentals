'''
Write a script that takes a list and turns it into a tuple.

'''

starting_list = [[1, 2, 3, 4], 'str_object', [5, 6], [7, 8, 9], 10, [11, [12, 13]]]
# starting_list = ['a']
'''
Because of difficulties previously mentioned, the list is not given by user input.
Practically, most often a list would be passed to a function rather than a user entering a literal list.

####################################
print("Example list: [1, 2, [6, 55], 2, 'hi', 4, 6, 1, 13]")
string_in = input("Enter your list: ")

string_in1 = string_in.replace(" ","") # removing whitespace from string
# this assumes there is no whitespace within a string in the list
#print(f"string without white space: {string_in1}")

starting_list = string_in1.strip('][').split(',')
####################################
'''

print(f"starting_list: {starting_list}")

'''
# Checking and troubleshooting:
for obj in starting_list:
    print(f"Object: {obj}, Type: {type(obj)}")
'''
#####################################################################
# If there are sub-lists within in the list, it may make sense to convert them to sub-tuples.
# However sub-sub-lists will remain as sub-sub-lists, which may then be confusing.
# It doesn't make sense to convert strings, integers or floats to tuples though.
# If it is not desired to convert sub-lists to sub-tuples, the code between these hashed lines should be commented out.
for i in range(len(starting_list)):
    if isinstance(starting_list[i], list):  # if there are sublists in starting_list
        starting_list[i] = tuple(starting_list[i])  # sublists are converted to tuples
#####################################################################

# now the entire list is converted to a tuple
tuple_ = tuple(starting_list)
print(f"list as tuple: {tuple_}")
