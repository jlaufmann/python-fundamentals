'''
Write a script that demonstrates a try/except/else.

'''

# Exactly as for 09_02_calculator.py

print(f"\n##### QUOTIENT CALCULATOR #####")

while True:
	try:
		dividend = float(input(f"\nDividend: "))
		divisor = float(input(f"Divisor: "))
		result = dividend / divisor
	except ZeroDivisionError as zde:
		print(f"Zero Division Error: {zde}")
	except ValueError as ve:
		print(f"Value Error: {ve}")
	else:
		print(f"Result: {result}")