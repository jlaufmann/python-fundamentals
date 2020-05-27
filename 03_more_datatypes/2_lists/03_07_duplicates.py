'''

Write a script that removes all duplicates from a list.

'''
# get list from input
print('In the format: [1, 2, 3, 4, 3, 4, 5]')
string_in = input("Enter your list: ")

# Example List:
# list_ = [1, 2, 3, 4, 3, 4, 5]

string_in1 = string_in.replace(" ","") # removing whitespace from string
list_in = string_in1.strip('][').split(',') # splitting string into list
# because it wasn't specified what type of items are in the string, they will just be left as general
# if all elements were to be floats or integers I could present the list in a more appropriate form.
print(f"Your list: {list_in}")

# using the set() command changes the order of the list, this is not what I want.
# no_dups = set(list_in)

no_dupes = []
for item in list_in:
    if item in no_dupes:
        pass
    else:
        no_dupes.append(item)

print(f"List without duplicates: {no_dupes}")
