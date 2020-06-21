'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
print(f"\n##### QUOTIENT CALCULATOR #####")

while True:
	try:
		dividend = float(input(f"\nDividend: "))
		divisor = float(input(f"Divisor: "))
		result = dividend / divisor
	except ZeroDivisionError as zde:
		print(f"Error: {zde}")
	except ValueError as ve:
		print(f"Error: {ve}")
	else:
		print(f"Result: {result}")
