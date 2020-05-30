'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

i = 5
while i <= 1000:
    print(f"{i} ", end=' ')
    if i%100 == 0:
        print("")
    i += 5
