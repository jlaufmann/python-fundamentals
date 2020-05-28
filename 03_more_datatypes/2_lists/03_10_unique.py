'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

# Example list:
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

'''
All this stuff is commented out because it is just too difficult to get a string from user input without knowing
in advance exactly what may be in the list. And in any case it is more likely that a string would be passed to a
function rather than getting the user to input a string in string format.

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
list_ = list_in
'''

print(f"list_ = {list_}")

unique_list = []
for item in list_:
    if list_.count(item) == 1:
        unique_list.append(item)

print(f"unique_list = {unique_list}")
