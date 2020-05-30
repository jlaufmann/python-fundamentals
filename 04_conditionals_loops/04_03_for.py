'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

print("All odd numbers from 1-100:")
for i in list(range(1,100,2)):
    if i < 99:
        print(f"{i},", end=' ')
    else:
        print(f"{i}.")
