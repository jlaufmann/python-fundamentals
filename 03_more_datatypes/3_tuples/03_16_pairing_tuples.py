'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

nums_in = input("Enter a list of numbers separated by commas: ")
nums_list = nums_in.strip(',').split(',')
print(f"Number list = {nums_list}")
nums_list2 = [float(word) for word in nums_list] # could instead be converted to ints

nums_list2.sort()

if len(nums_list2)%2 != 0:
    nums_list2.append(0)

tup_list = []
for i in list(range(0, len(nums_list2), 2)):
    tup_list.append((nums_list2[i], nums_list2[i+1]))

# print(f"tup_list = {tup_list}")

print("Tuples are: ")
for tuplee in tup_list:
    print(tuplee)
