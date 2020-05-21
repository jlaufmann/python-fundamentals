'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

string = input('String input: ')
letter = input('Letter input: ')
result = string.find(letter)
result2 = string.index(letter)
print('Index of first occurence of letter in string: \n', result)
