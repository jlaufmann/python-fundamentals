'''
Print out every prime number between 1 and 100.

'''

prime = []

for i in range(1,100):
    flag = 0
    for j in range(2, i//2 + 1):
        if (i % j) == 0:
            flag = 1
    if flag == 0:
        prime.append(i)

print("Prime numbers between 1 and 100: ")
for num in prime:
    print(f"{num}", end=' ')

