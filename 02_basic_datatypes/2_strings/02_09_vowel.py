'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
string = input('Enter your string: ').lower()

'''
# Contained here is an improved method I discovered later
a_count = string.count('a')
e_count = string.count('e')
i_count = string.count('i')
o_count = string.count('o')
u_count = string.count('u')
'''

a_count, e_count, i_count, o_count, u_count = 0, 0, 0, 0, 0

for letter in string:
    if letter == 'a':
        a_count += 1
    elif letter == 'e':
        e_count += 1
    elif letter == 'i':
        i_count += 1
    elif letter == 'o':
        o_count += 1
    elif letter == 'u':
        u_count += 1

v_count = a_count + e_count + i_count + o_count + u_count
print('There are ', v_count, 'vowels in the string.')
print("Number of A's: ", a_count)
print("Number of E's: ", e_count)
print("Number of I's: ", i_count)
print("Number of O's: ", o_count)
print("Number of U's: ", u_count)
