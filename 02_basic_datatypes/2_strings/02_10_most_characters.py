'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

string1 = input('String 1: ')
string2 = input('String 2: ')
string3 = input('String 3: ')

print(str(len(string1)) + ', ' + string1)
print(str(len(string2)) + ', ' + string2)
print(str(len(string3)) + ', ' + string3)

print('\n===== Printing only the string(s) with the most characters =====')
max_len = max(len(string1), len(string2), len(string3))
if len(string1) == max_len:
    print(str(len(string1)) + ', ' + string1)
if len(string2) == max_len:
    print(str(len(string2)) + ', ' + string2)
if len(string3) == max_len:
    print(str(len(string3)) + ', ' + string3)
