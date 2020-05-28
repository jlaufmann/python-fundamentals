'''

Write a script that removes all duplicates from a list.

'''

# Example List:
list_ = [1, 2, 6, 3, 4, 3, 4, 5]

'''
Because of the difficulty of getting strings from user input I have commented out all this stuff and will just use an
example list supplied in the script. In any case, in most cases it would be unlikely that a user should directly
enter a string, but a string would be passed to a function, and functions like that haven't been covered here yet.

# get list from input
print('In the format: [1, 2, 3, 4, 3, 4, 5]')
string_in = input("Enter your list: ")

string_in1 = string_in.replace(" ","") # removing whitespace from string
list_in = string_in1.strip('][').split(',') # splitting string into list
# because it wasn't specified what type of items are in the string, they will just be left as general
# if all elements were to be floats or integers I could present the list in a more appropriate form.

list_ = list_in
'''

print(f"Initial list: {list_}")

# using the set() command may change the order of the list, and this is not desired here
# no_dups = set(list_in)

no_dupes = []
for item in list_:
    if item in no_dupes:
        pass
    else:
        no_dupes.append(item)

print(f"List without duplicates: {no_dupes}")
