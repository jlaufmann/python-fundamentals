'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

string_in = input("Enter your string: ")
# so that A and a are the same, convert string to lower case.
string_l = string_in.lower()

keys = []
for char in string_l:
    if char.isalpha() and (char not in keys):
        keys.append(char)

# it could be nice to sort the letters alphabetically
keys.sort()

'''
strings are immutable, lists are mutable.
string.lower() needs to be assigned to new_string - because strings are immutable
string.sort() does not work
list.lower() does not work
list.sort() does not need an assignment. An assignment in the statement will not work!!
list2 = sorted(list) leaves list unsorted, and assigns the sorted list to list2.
'''

my_dict = {}
for letter in keys:
    my_dict[letter] = string_l.count(letter)

print(f"result = {my_dict}")
