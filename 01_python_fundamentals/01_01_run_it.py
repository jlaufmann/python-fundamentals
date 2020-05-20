'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''

#1
# see file hello.py

#2
'''
$ python3
>>> print("hello world!")
'''

#3
'''
print("no 2nd quotation mark)

print("no 2nd paranthesis"

we get syntax errors
the error messages are good, in these examples they tell us where to look to correct the error
'''

'''
$ python3
>>> help(print)
'''

'''
$ python3
>>> 2 + 2

>>> days_in_year = 365
>>> hours_in_day = 24 
>>> minutes_in_hour = 60
>>> seconds_in_minute = 60 
>>> seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
>>> print(seconds_in_year)
31536000
'''
