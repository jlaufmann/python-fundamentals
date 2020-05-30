'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

magic_no = int(input("Enter an integer number between 0 and 1,000,000,000: "))

method = 'simple'
# method = 'fast'

guess_low = 0
guess_high = 1E+9

if magic_no < guess_low or magic_no > guess_high:
    print("That number is out of range!")
    quit()

guess = 0

########### SIMPLE METHOD ##########
if method == 'simple':
    while guess != magic_no:
        guess += 1
##############################################

# that is the simplest method, but on my computer can take up to 80 seconds to find the magic_no
# using if loops to implement upper and lower bounds each time is much quicker.

########## FAST METHOD #############
if method == 'fast':
    while guess != magic_no:
        guess = int(((guess_high - guess_low) // 2) + guess_low)
        if magic_no < guess:
            guess_high = guess
        elif magic_no > guess:
            guess_low = guess
##############################################

print(f"Your number is: {guess}")
