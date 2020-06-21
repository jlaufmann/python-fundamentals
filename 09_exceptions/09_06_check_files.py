'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

with open(file_name, 'r') as fin0:
	ints = fin0.read().split('\n')
	# ints = fin0.read()
	try: 
		int2 = int(ints[0])
	except IOError as io_err:
		print(f"IOError! - {io_err}")
	except ValueError as v_err:
		print(f"ValueError! - {v_err}")
	except Exception as exc:
		print(f"EXCEPTION! - {exc}")
	else:
		print(f"i = {int2}")
		print(f"i^2 = {int2**2}")
