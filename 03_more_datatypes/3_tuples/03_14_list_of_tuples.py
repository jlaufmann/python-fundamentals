'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

in_string = input("Please input your string: ")
print(f"input = {in_string}")
#print(f"in_string = {in_string}, type = {type(in_string)}")
word_list = in_string.split()
#print(f"word_string = {word_list}, type = {type(word_list)}")

result_list = [tuple(word) for word in word_list]
'''
result_list = []
for word in word_string:
    result_list.append(tuple(list(word)))
'''
print(f"result_list = {result_list}")
#print(f"result_list = {result_list}, type(result_list) = {type(result_list)}")

'''
for word in result_list:
    print(f"word = {word}, type(word) = {type(word)}")
'''
