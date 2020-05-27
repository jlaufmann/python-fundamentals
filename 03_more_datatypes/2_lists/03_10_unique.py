'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
# get list from input:
print("Example list: [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]")
string_in = input("Enter your list: ")

string_in1 = string_in.replace(" ","") # removing whitespace from string
# this assumes there is no whitespace within a string in the list
#print(f"string without white space: {string_in1}")

list_in = string_in1.strip('][').split(',') # splitting string into list
#print(f"string split into list: {list_in}")
#print(type(list_in))

# Because the list may contain integers, floats or strings, all items will just be treated as general items

# Example list:
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = []

for item in list_in:
    if list_in.count(item) == 1:
        unique_list.append(item)

print(f"Unique list: {unique_list}")
