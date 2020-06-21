'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

isint = False
while not isint:
	try:
		mynum = float(input(f"Enter an integer: "))
	except:
		print(f"That's not an integer") 
	else:
		if mynum % 1 == 0:
			print(f"Thank-you for your integer!")
			isint = True
		else:
			print(f"That's not an integer")
