'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# This needs work too most likely!!!!!!!!!!!!!!!!!!!!
in_string = input("Please input your string: ")
print(in_string)
word_string = in_string.split()
print(type(word_string))
print(word_string)

result_list = []
for word in word_string:
    result_list.append(tuple(list(word)))

print(f"result_list = {result_list}")
