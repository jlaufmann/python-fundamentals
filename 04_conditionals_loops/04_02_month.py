'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

my_num = float(input("Enter a number: "))

if my_num == 1:
    print("January")
elif my_num == 2:
    print("February")
elif my_num == 3:
    print("March")
elif my_num == 4:
    print("April")
elif my_num == 5:
    print("May")
elif my_num == 6:
    print("June")
elif my_num == 7:
    print("July")
elif my_num == 8:
    print("August")
elif my_num == 9:
    print("September")
elif my_num == 10:
    print("October")
elif my_num == 11:
    print("November")
elif my_num == 12:
    print("December")
else:
    print("Other")
