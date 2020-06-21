'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''
'''
#1: 
with open('books/war_and_peace.txt', 'r') as fin0:
	wap = fin0.readlines()

# print(f"{wap}")

#2:
with open('books/crime_and_punishment.txt', 'w') as fin1:
	fin1.write('')
'''

import os

class PrinceExcept(Exception):
	pass

fol_in = 'books'

for filename in os.listdir(fol_in):
	if os.path.isfile(os.path.join(fol_in, filename)):
		# print(f"\nfile: {filename}")
		with open(os.path.join(fol_in, filename)) as fin:
			try:
				mystring = fin.read()
				if 'Prince' in mystring[1:100]:
					raise PrinceExcept('Prince found!')
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				# print(f"1st char: {mystring[1]}")
				print(f"{mystring[1]}")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")

# in all the above stuff I am printing the 1th rather than 0th character.
# this is because I don't know the encoding of these text files, and so
# the 0th character is actually: '\ufeff'


'''
			try:
				line1 = fin.readline().rstrip('\n')
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"type(line1) = {type(line1)}")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"line1 = '{line1}'")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"line1[0] = '{line1[0]}'")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")

			try:
				line2 = fin.readline().rstrip('\n')
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"type(line2) = {type(line2)}")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"line2 = '{line2}'")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")
			try:
				print(f"line2[0] = '{line2[0]}'")
			except Exception as exc:
				print(f"EXCEPTION: {exc}")

# I don't understand why the 0th objects in the strings are showing as nothing.			
'''
